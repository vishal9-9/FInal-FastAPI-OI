from database import databaseHelper
from fastapi import HTTPException
from http import HTTPStatus
from config import logError

def add_new_company(data,cur_user):
    if databaseHelper.validate_comp_name(data.company_name):
       raise HTTPException(status_code = HTTPStatus.ALREADY_REPORTED, detail = logError.COMPANY_ALREADY_REGISTERED)
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        try:
            databaseHelper.add_new_company(data)
            raise HTTPException(status_code = HTTPStatus.OK, detail = logError.COMPANY_ADDED_SUCCESSFULLY)
        except:
            raise HTTPException(status_code = HTTPStatus.BAD_REQUEST, detail = logError.ADDING_ERROR)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)