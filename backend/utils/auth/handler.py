# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict
from decouple import config
from jose import jwt

# fix env
JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")


def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + (60 * 60 * 24 * 7) # 7 days expiration time
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if 'user_id' in decoded_token and decoded_token["expires"] >= time.time():
            return decoded_token['user_id']
        else:
            return None
    except:  # noqa: E722 can add some error codes here and such
        return None
