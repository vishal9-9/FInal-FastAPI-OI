from database import databaseHelper
from http import HTTPStatus
from fastapi import HTTPException
from config import logError

def update_user(id: int,user,cur_user):
    email_already_present = databaseHelper.update_email_check(id)
    if user.email in email_already_present:
        raise HTTPException(status_code = HTTPStatus.CONFLICT)
    company_id = databaseHelper.list_of_cid()
    if user.c_id not in company_id:
        raise HTTPException(status_code = HTTPStatus.BAD_REQUEST)
    role = databaseHelper.role_power(cur_user.id)
    user_toupdate = databaseHelper.list_user_id(id)
    if not user_toupdate:
        raise HTTPException(status_code = HTTPStatus.NOT_FOUND)
    if role == 'Superadmin':
        if user.role_id in [1,2,3] and user.role_id < user_toupdate.role_id:
            if user.role_id == 3:
                check_bool = databaseHelper.role_power(user.working_under)
                if check_bool == 'Supervisor':
                    databaseHelper.update_user(user,id)
                    return logError.UPDATED_USER_SUCCESSFULLY
                else:
                    return logError.WORKING_UNDER_IS_NOT_A_SUPERVISOR
            elif user.role_id == 2:
                check_bool = databaseHelper.role_power(user.working_under)
                if check_bool == 'Admin':
                    databaseHelper.update_user(user,id)
                    return logError.UPDATED_USER_SUCCESSFULLY
                else:
                    return logError.WORKING_UNDER_IS_NOT_A_ADMIN
            elif user.role_id == 1:
                user.working_under = cur_user.id
                databaseHelper.update_user(user,id)
                return logError.UPDATED_USER_SUCCESSFULLY
        else:
            raise HTTPException(status_code = HTTPStatus.BAD_REQUEST)
    elif role == 'Admin':
        if cur_user.c_id == user_toupdate.c_id:
            if cur_user.role_id < user_toupdate.role_id:
                if user.role_id in [2,3] and user.c_id == cur_user.c_id:
                    if user.role_id == 2:
                        check_bool = databaseHelper.role_power(user.working_under)
                        if check_bool == 'Admin':
                            databaseHelper.update_user(user,id)
                            return logError.UPDATED_USER_SUCCESSFULLY
                        else:
                            return logError.WORKING_UNDER_IS_NOT_A_ADMIN
                    elif user.role_id == 3:
                        check_bool = databaseHelper.role_power(user.working_under)
                        if check_bool == 'Supervisor':
                            databaseHelper.update_user(user,id)
                            return logError.UPDATED_USER_SUCCESSFULLY
                        else:
                            return logError.WORKING_UNDER_IS_NOT_A_SUPERVISOR                       
                else:
                    raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
            else:
                raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
        else:
            raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
    elif role == 'Supervisor':
        if cur_user.c_id == user_toupdate.c_id:
                if user.role_id in [3] and cur_user.role_id < user_toupdate.role_id and user.c_id == cur_user.c_id:
                    if user.role_id == 3:
                        check_bool = databaseHelper.role_power(user.working_under)
                        if check_bool == 'Supervisor':
                            databaseHelper.update_user(user,id)
                            return logError.UPDATED_USER_SUCCESSFULLY
                        else:
                            return logError.WORKING_UNDER_IS_NOT_A_SUPERVISOR
                    else:
                        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
                else:
                    raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
        else:
            raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)