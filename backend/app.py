# SHOULD BE RUN SEPARATELY

from __future__ import annotations
from typing import Any, Callable

import uvicorn
from asyncpg import Pool, Record, create_pool
from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from utils import ENV

pool: Pool[Record] | None = None
ml_models: dict[Callable[..., Any | None]] = {}

async def create_db_pool() -> Pool[Record]:
    credentials = {
        "user": ENV["PG_USERNAME"],
        "password": ENV["PG_PASSWORD"],
        "database": ENV["PG_NAME"],
        "host": ENV["PG_HOST"],
        "port": ENV["PG_PORT"],
    }
    return await create_pool(**credentials)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    #ml_models["create_db_pool"] = create_db_pool
    global pool
    pool = await create_db_pool()

    yield

    # Clean up the ML models and release the resources
    ml_models.clear()

app = FastAPI(lifespan=lifespan)

origins = [ # change to the actual domain later
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='https://.*\.dwello\.bot',
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SignupForm(BaseModel): # no idea how this works yet
    email: str
    password: str
    day: dict[str, str]
    month: dict[str, str]
    year: dict[str, str]


# EXAMPLE: PRINT ANY POST REQUEST DATA
@app.post("/signup")
async def root(request: Request):
    print("root here")
    data = await request.json()
    print(data)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)