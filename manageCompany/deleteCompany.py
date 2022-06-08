from database import databaseHelper
from fastapi import HTTPException
from http import HTTPStatus
from config import logError

def del_company(cur_user,id: int):
    if id == 0:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)
    company_id = databaseHelper.list_of_cid()
    if id not in company_id:
        raise HTTPException(status_code = HTTPStatus.NOT_FOUND, detail = logError.COMPANY_NOT_FOUND)
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        try:
            databaseHelper.delete_compnany(id)
            return HTTPException(status_code = HTTPStatus.CREATED, detail = logError.COMPANY_DELETED_SUCCESSFULLY)
        except:
            raise HTTPException(status_code = HTTPStatus.BAD_REQUEST, detail = logError.ADDING_ERROR)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)