from database import databaseHelper
from http import HTTPStatus
from fastapi import HTTPException
from config import logError

def add_user(user,cur_user):
    already_exist = databaseHelper.if_user_exist(user.email)
    if already_exist:
        raise HTTPException(status_code = HTTPStatus.CONFLICT, detail = logError.USER_IS_ALREADY_REGISTERED_WITH_US)
    company_id = databaseHelper.list_of_cid()
    if user.c_id not in company_id:
        raise HTTPException(status_code = HTTPStatus.BAD_REQUEST, detail = logError.COMPANY_NOT_FOUND)
    check_workingUnder = databaseHelper.role_power(user.working_under)
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        if user.role_id in [1,2,3]:
            if user.role_id == 3:
                if check_workingUnder == 'Supervisor':
                    databaseHelper.add_new_user(user)
                    return HTTPException(status_code = HTTPStatus.CREATED, detail = logError.USER_ADDED_SUCCESSFULLY)
                else:
                    return HTTPException(status_code = HTTPStatus.FORBIDDEN, detail = logError.WORKING_UNDER_IS_NOT_A_SUPERVISOR)
            elif user.role_id == 2:
                if check_workingUnder == 'Admin':
                    databaseHelper.add_new_user(user)
                    return HTTPException(status_code = HTTPStatus.CREATED, detail = logError.USER_ADDED_SUCCESSFULLY)
                else:
                    return HTTPException(status_code = HTTPStatus.FORBIDDEN, detail = logError.WORKING_UNDER_IS_NOT_A_ADMIN)
            elif user.role_id == 1:
                user.working_under = 1
                databaseHelper.add_new_user(user)
                return HTTPException(status_code = HTTPStatus.CREATED, detail = logError.USER_ADDED_SUCCESSFULLY)
        else:
            return logError.INVALID_ROLE_ERROR
    elif role == 'Admin':
        user.c_id = cur_user.c_id
        if user.role_id in [2,3]:
            if user.role_id == 3:
                if check_workingUnder == 'Supervisor':
                    user.c_id = cur_user.c_id
                    databaseHelper.add_new_user(user)
                    return HTTPException(status_code = HTTPStatus.CREATED, detail = logError.USER_ADDED_SUCCESSFULLY)
                else:
                    return HTTPException(status_code = HTTPStatus.FORBIDDEN, detail =logError.WORKING_UNDER_IS_NOT_A_SUPERVISOR)
            elif user.role_id == 2:
                if check_workingUnder == 'Admin':
                    databaseHelper.add_new_user(user)
                    return HTTPException(status_code = HTTPStatus.CREATED, detail = logError.USER_ADDED_SUCCESSFULLY)
                else:
                    return HTTPException(status_code = HTTPStatus.FORBIDDEN, detail = logError.WORKING_UNDER_IS_NOT_A_ADMIN)
        else:
            return HTTPException(status_code = HTTPStatus.FORBIDDEN, detail = logError.INVALID_ROLE_ERROR)
    elif role == 'Supervisor':
        user.c_id = cur_user.c_id
        if user.role_id in [3]:
            if user.role_id == 3:
                if check_workingUnder == 'Supervisor' and cur_user.c_id == user.c_id:
                    databaseHelper.add_new_user(user)
                    return HTTPException(status_code = HTTPStatus.CREATED, detail = logError.USER_ADDED_SUCCESSFULLY)
                else:
                    return HTTPException(status_code = HTTPStatus.FORBIDDEN, detail = logError.WORKING_UNDER_IS_NOT_A_SUPERVISOR)
        else:
            return HTTPException(status_code = HTTPStatus.FORBIDDEN, detail = logError.INVALID_ROLE_ERROR)
    else:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail = logError.USER_IS_UNAUTHORISED)