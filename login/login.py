import json
from config import logError
from database import databaseHelper
from helpers import passhash,tokens
from fastapi import HTTPException
from http import HTTPStatus

def login_user(request):
    user = databaseHelper.if_user_exist(request.email)
    if user is None:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.INVALID_CREDENTIALS)
    if not user.isactive == 1:
        raise HTTPException(status_code = HTTPStatus.FORBIDDEN, detail = logError.USER_IS_INACTIVE)
    psswd = request.password
    password = passhash.check_hash(psswd,user.password)
    if not password:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.INVALID_CREDENTIALS)
    to_tokenize = {
        'email' : user.email,
        'company_id' : user.c_id,
        'fullname' : user.fullname,
        'role_id' : user.role_id,
        'contact_no' : user.contact_no,
        'working_under' : user.working_under
    }
    to_tokenize = json.dumps(to_tokenize)
    access_token = tokens.create_access_token(data = {'sub': to_tokenize})
    return {"access_token" : access_token , "token_type": "bearer"}