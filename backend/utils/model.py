from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional

from datetime import datetime


class PostSchema(BaseModel):
    id: int = Field(default=None, ge=1)  # Use ge=1 to ensure id is always greater than or equal to 1
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens...."
            }
        }

class UserSchema(BaseModel):
    # can add stuff like this later on
    # date of birth; maybe some additional personal data

    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    day: int = Field(...)
    month: int = Field(...)
    year: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "Joe Doe",
                "email": "joe@xyz.com",
                "password": "any"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                "password": "any"
            }
        }


class EmailSchema(BaseModel):
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
            }
        }


class PasswordSchema(BaseModel):
    new_password: str = Field(...)
    confirm_password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "new_password": "abc123",
                "confirm_password": "abc123",
            }
        }


class ZohoEmailSchema(BaseModel):
    # based off of https://www.zoho.com/mail/help/api/post-send-an-email.html

    toAddress: EmailStr = Field(...)
    fromAddress: EmailStr

    ccAddress: Optional[EmailStr] = None
    bccAddress: Optional[EmailStr] = None
    subject: Optional[str] = None
    content: Optional[str] = "Just testing. Sorry for the inconvenience!"
    encoding: Optional[Literal[
        "Big5",
        "EUC-JP",
        "EUC-KR",
        "GB2312",
        "ISO-2022-JP",
        "ISO-8859-1",
        "KOI8-R",
        "Shift_JIS",
        "US-ASCII",
        "UTF-8", # default
        "WINDOWS-1251",
        "X-WINDOWS-ISO2022JP",
    ]] = None
    mailFormat: Optional[Literal["html", "plaintext"]] = None # "html" is default
    askReceipt: Optional[Literal["yes"]] = None # "yes" is default

    # read the docs to pass the values correctly
    isSchedule: Optional[bool] = None
    scheduleType: Optional[Literal[1, 2, 3, 4, 5, 6]] = None
    timeZone: Optional[str] = None # maybe datetime in the future
    scheduleTime: Optional[datetime] = None # MM/DD/YYYY HH:MM

