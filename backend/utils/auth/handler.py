# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict

import jwt
#from ..environment import ENV

# fix env
JWT_SECRET = "2a816a087989e32b5fbda8799ee4aab84a4866625c00480c81fb6ed86be95559" #ENV("JWT_SECRET")
JWT_ALGORITHM = "HS256" #ENV("JWT_ALGORITHM")


def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:  # noqa: E722 can add some error codes here and such
        return {}