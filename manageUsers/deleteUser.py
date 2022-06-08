from database import databaseHelper
from fastapi import HTTPException
from http import HTTPStatus

def users_delete(cur_user,id: int):
    if id == 1:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
    to_delete = databaseHelper.list_user_id(id)
    if not to_delete:
        raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        return databaseHelper.delete_user_superadmin(id)
    elif role == 'Admin':
        if cur_user.c_id == to_delete.c_id:
            return databaseHelper.delete_user_admin(id)
        else:
            raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
    elif role == 'Supervisor':
        if cur_user.c_id == to_delete.c_id:
            return databaseHelper.delete_user_supervisor(id)
        else:
            raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)