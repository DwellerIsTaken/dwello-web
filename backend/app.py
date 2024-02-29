# SHOULD BE RUN SEPARATELY

from __future__ import annotations
from typing import Any, Callable

import uvicorn
import aiofiles
import aiohttp
from decouple import Config
from datetime import date
from asyncpg import Pool, Record, create_pool
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Body, Depends  # noqa: F401
from fastapi.middleware.cors import CORSMiddleware

from utils import ENV, UserSchema, UserLoginSchema, ZohoEmailSchema, signJWT

config = Config(".env")

ZOHO_CLIENT_ID = config("ZOHO_CLIENT_ID")
ZOHO_ACCOUNT_ID = config("ZOHO_ACCOUNT_ID")
ZOHO_CLIENT_SECRET = config("ZOHO_CLIENT_SECRET")
ZOHO_REFRESH_TOKEN = config("ZOHO_REFRESH_TOKEN")
ZOHO_BASE_ACCOUNTS_URL = config('ZOHO_BASE_ACCOUNTS_URL')

# keep it within some class maybe, instead of making it a global var
pool: Pool[Record] | None = None
ml_models: dict[Callable[..., Any | None]] = {}

session: aiohttp.ClientSession | None = None

'''class MySession:
    def __init__(self, session):
        self._session = session

async def build_session():
    return MySession(aiohttp.ClientSession())'''

async def check_user(data: UserLoginSchema) -> bool:
    async with pool.acquire() as conn:
        if record:= await conn.fetchrow("SELECT email, password FROM client_data WHERE email = $1", data.email):
            if data.email == record['email'] and data.password == record['password']:
                return True
    return False

async def create_db_pool() -> Pool[Record]:
    credentials = {
        "user": ENV["PG_USERNAME"],
        "password": ENV["PG_PASSWORD"],
        "database": ENV["PG_NAME"],
        "host": ENV["PG_HOST"],
        "port": ENV["PG_PORT"],
    }
    return await create_pool(**credentials)

async def create_tables() -> None:
    async with pool.acquire() as conn:
        async with aiofiles.open("schema.sql", encoding="utf-8") as f:
            await conn.execute(await f.read())

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    #ml_models["create_db_pool"] = create_db_pool
    global pool, session
    pool = await create_db_pool()
    await create_tables()
    session = aiohttp.ClientSession()

    yield

    # Clean up the ML models and release the resources
    ml_models.clear()

app = FastAPI(lifespan=lifespan)

origins = [ # change to the actual domain later
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    #allow_origin_regex='https://.*\.dwello\.bot',
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


# EXAMPLE: PRINT ANY POST REQUEST DATA
'''@app.post("/signup")
async def signup(request: Request):
    data: dict[str, str] = await request.json()
    email = data.get("email")
    password = data.get("password")

    async with pool.acquire() as conn:
        if record:= await conn.fetchrow("SELECT email, password FROM client_data WHERE email = $1", email):
            if record['email'] == email:
                return {"message": "You already have an account, please log in."}
        await conn.execute("INSERT INTO client_data (email, password) VALUES ($1, $2)", email, password)
    
    # You may want to return a success response here
    return {"message": "Signup successful"}'''


@app.post("/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    # if valid email adress isnt entered, the 422 arises
    # can make a style for that

    # replace with db call, making sure to hash the password first
    # do some checks, return token eventually

    async with pool.acquire() as conn:
        if record:= await conn.fetchrow("SELECT email, password FROM client_data WHERE email = $1", user.email):
            if record['email'] == user.email:
                return {
                    "message": "You already have an account, please log in."
                }
        await conn.execute(
            "INSERT INTO client_data (email, password, birth_date) VALUES ($1, $2, $3)",
            user.email, user.password, date(user.year, user.month, user.day),
        )

    # returns a token!!!
    return signJWT(user.email)


@app.post("/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if await check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

async def send_an_email(access_token: str, email: ZohoEmailSchema):
    url = f"https://mail.zoho.eu/api/accounts/{ZOHO_ACCOUNT_ID}/messages"
    headers = {"Authorization": f"Zoho-oauthtoken {access_token}"}
    data = {
        key: value
        for key, value in {
            "toAddress": email.toAddress,
            "fromAddress": email.fromAddress,
            "ccAddress": email.ccAddress,
            "bccAddress": email.bccAddress,
            "subject": email.subject,
            "encoding": email.encoding,
            "mailFormat": email.mailFormat,
            "askReceipt": email.askReceipt,
            "isSchedule": email.isSchedule,
            "scheduleType": email.scheduleType,
            "timeZone": email.timeZone,
            "scheduleTime": email.scheduleTime,
            "content": email.content, # whether its an html or plaintext
        }.items()
        if value is not None
    }
    async with session.post(url, headers=headers, json=data) as response:
        response_data = await response.json()
        print(response.status)
        print(response_data)

    return response

@app.post("/send_email", tags=["email"])
async def send_email(email: ZohoEmailSchema = Body(...)):
    response = await send_an_email(config("ZOHO_ACCESS_TOKEN"), email)
    match response.status:
        case 400:
            # expired access token
            async with session.post(
                f"https://{ZOHO_BASE_ACCOUNTS_URL}/oauth/v2/token?refresh_token={ZOHO_REFRESH_TOKEN}&client_id={ZOHO_CLIENT_ID}&client_secret={ZOHO_CLIENT_SECRET}&grant_type=refresh_token",
            ) as _response:
                new_access_token = await _response.json()
                print(_response.status, _response)

        case _:
            # redirect to the page with that error code
            ...
        
    await send_an_email(new_access_token["access_token"], email)

'''async def main():
    my_session = await build_session()'''

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) 