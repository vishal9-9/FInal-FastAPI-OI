from jose import jwt
from http import HTTPStatus
from fastapi import HTTPException

SECRET_KEY = 'b3a94dceab794d6f6d57f711096c7fbd4083d6fcb44209f7be5458e373d9ce79'

def create_access_token(data: dict):
    to_encode = data.copy()
    try:
        token = jwt.encode(to_encode,SECRET_KEY)
        return token
    except:
        raise HTTPException(status_code = HTTPStatus.NOT_ACCEPTABLE)

def decode_access_token(token: str):
    try:
        return jwt.decode(token,SECRET_KEY)
    except:
        raise HTTPException(status_code = HTTPStatus.NOT_ACCEPTABLE)