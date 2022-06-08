from database import databaseHelper
from http import HTTPStatus
from fastapi import HTTPException

def supervisor_list(cur_user):
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        res = databaseHelper.list_supervisor_superadmin()
        if res:
            return res
        else:
            raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    elif role in ['Admin','Supervisor']:
        res = databaseHelper.list_supervisor_admin_supervisor(cur_user.c_id)
        if res:
            return res
        else:
            raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)