from database import databaseHelper
from http import HTTPStatus
from fastapi import HTTPException

def list_user(cur_user):
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        users =  databaseHelper.list_all_user()
        if users:
            return users
        else:
            raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    elif role == 'Admin':
        users = databaseHelper.list_user_admin(cur_user)
        if users:
            return users
        else:
            raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    elif role == 'Supervisor':
        users = databaseHelper.list_user_supervisor(cur_user)
        if users:
            return users
        else:
            raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)


def list_user_id(id: int,cur_user):
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        user = databaseHelper.list_user_id(id)
        if user:
            return user
        else:
            raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    elif role == 'Admin':
        user =  databaseHelper.list_user_id_admin(id,cur_user)
        if user:
            return user
        else:
            raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    elif role == 'Supervisor':
        user =  databaseHelper.list_user_id_supervisor(id,cur_user)
        if user:
            return user
        else:
            raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    else:
        raise HTTPException(HTTPStatus.UNAUTHORIZED)