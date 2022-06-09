from config import logError
from database import databaseHelper
from fastapi import HTTPException
from http import HTTPStatus

def users_delete(cur_user,id: int):
    role = databaseHelper.role_power(cur_user.id)
    if role == 'User':
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)
    if id == 1:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)
    to_delete = databaseHelper.list_user_id(id)
    if not to_delete:
        raise HTTPException(status_code = HTTPStatus.NOT_FOUND, detail = logError.USER_NOT_FOUND)
    if role == 'Superadmin':
        return databaseHelper.delete_user_superadmin(id)
    elif role == 'Admin':
        if cur_user.c_id == to_delete.c_id:
            return databaseHelper.delete_user_admin(id)
        else:
            raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_DOES_NOT_WORK_UNDER_YOUR_COMPANY)
    elif role == 'Supervisor':
        if cur_user.c_id == to_delete.c_id:
            return databaseHelper.delete_user_supervisor(id)
        else:
            raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_DOES_NOT_WORK_UNDER_YOUR_COMPANY)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)