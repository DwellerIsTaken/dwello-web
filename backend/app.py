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
from fastapi import HTTPException, FastAPI, Request, status, Body, Depends  # noqa: F401
from fastapi.middleware.cors import CORSMiddleware
from utils import ENV, UserSchema, UserLoginSchema, ZohoEmailSchema, EmailSchema, PasswordSchema, signJWT, decodeJWT
from jose import JWTError


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


async def check_user(data: UserLoginSchema) -> bool:
    async with pool.acquire() as conn:
        if record:= await conn.fetchrow("SELECT email, password FROM client_data WHERE email = $1", data.email):
            if data.email == record['email'] and data.password == record['password']:
                return True
    return False


async def get_user_by_email(email):
    async with pool.acquire() as conn:
        if record:= await conn.fetchrow("SELECT * FROM client_data WHERE email = $1", email):
            return record
    return None


async def update_user_password(email: str, new_password: str) -> bool:
    try:
        async with pool.acquire() as conn:
            existing_user = await conn.fetchrow("SELECT * FROM client_data WHERE email = $1", email)
            if existing_user:
                await conn.execute("UPDATE client_data SET password = $1 WHERE email = $2", new_password, email)
                return True
        return False
    except:  # noqa: E722
        return False


async def validate_token(request: Request):
    try:
        email = decodeJWT(request.headers.get('Authorization', ''))
        user = await get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token!",
            )
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token!")


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
    return { # return an http exception 401
        "error": "Wrong login details!"
    }


@app.get("/profile")
def user_profile(request: Request, current_user = Depends(validate_token)):
    return {"user": current_user}


@app.post("/reset-password")
async def reset_password(data: EmailSchema):
    user = await get_user_by_email(data.toAddress)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found with this email!",
        )

    token = signJWT(data.toAddress)
    return {"link": f"http://localhost:5173/update-password?token={token['access_token']}"}


@app.put("/update-password")
async def update_password(data: PasswordSchema, current_user = Depends(validate_token)):
    if data.new_password != data.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password must match with the confirm password!",
        )

    is_updated = await update_user_password(current_user['email'], data.new_password)

    if not is_updated:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong!",
        )

    return {"response": "Password updated successfully!"}


async def send_an_email(access_token: str, email: ZohoEmailSchema):
    user = await get_user_by_email(email.toAddress)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found with this email!",
        )

    token = signJWT(email.toAddress)
    reset_password_link = f"http://localhost:5173/update-password?token={token['access_token']}"

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
            "content": reset_password_link, # whether its an html or plaintext, #email.content
            #"resetPasswordLink": reset_password_link # you can pass the password renewal link as a parameter, or just put it in here for now and ill expand everything later
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