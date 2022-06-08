import json
from http import HTTPStatus
from fastapi.security import OAuth2PasswordBearer
from database.engine import session
from models import models
from fastapi import Depends, HTTPException
from helpers import tokens

oauth_scheme = OAuth2PasswordBearer(tokenUrl = 'login')

db = session

def current_user(token: str = Depends(oauth_scheme)):
        payload = tokens.decode_access_token(token)
        decoded_token = payload.get('sub')
        try:
            user_details = json.loads(decoded_token)
        except:
            raise HTTPException(status_code = HTTPStatus.NOT_ACCEPTABLE)
        email: str = user_details.get('email')
        if email is None:
            raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
        else:
            user = db.query(models.Users).filter( models.Users.email == email ).first()
            if user is None:
                raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
            else:
                return user