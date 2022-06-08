from database import databaseHelper
from fastapi import HTTPException
from http import HTTPStatus
from config import logError

def add_new_company(data,cur_user):
    if databaseHelper.validate_comp_name(data.company_name):
       raise HTTPException(status_code = HTTPStatus.ALREADY_REPORTED)
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        try:
            databaseHelper.add_new_company(data)
            return logError.COMPANY_ADDED_SUCCESSFULLY
        except:
            raise HTTPException(status_code = HTTPStatus.BAD_REQUEST)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)