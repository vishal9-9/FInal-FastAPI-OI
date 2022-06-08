from config import logError
from database import databaseHelper
from fastapi import HTTPException
from http import HTTPStatus

def list_of_company(cur_user):
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        res = databaseHelper.list_company_superadmin()
        if res:
            return res
        else:
            raise HTTPException(status_code = HTTPStatus.NO_CONTENT, detail = logError.COMPANY_NOT_FOUND)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)

def list_of_company_id(cur_user,id: int):
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        res = databaseHelper.list_company_superadmin_id(id)
        if res:
            return res
        else:
            raise HTTPException(status_code = HTTPStatus.NOT_FOUND, detail = logError.COMPANY_NOT_FOUND)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)