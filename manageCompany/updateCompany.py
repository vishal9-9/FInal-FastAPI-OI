from database import databaseHelper
from fastapi import HTTPException
from http import HTTPStatus
from config import logError

def update_company(data,cur_user,id):
    if databaseHelper.validate_comp_name(data.company_name):
       raise HTTPException(status_code = HTTPStatus.ALREADY_REPORTED, detail = logError.COMPANY_ALREADY_REGISTERED)
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        databaseHelper.update_company(data,id)
        return HTTPException(status_code = HTTPStatus.ACCEPTED, detail = logError.COMPANY_UPDATED_SUCCESSFULLY)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)