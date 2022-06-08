from typing import List
from fastapi import APIRouter, Depends
from manageUsers import addUser, listUser, updateUser, listSupervisor, deleteUser
from login.oauth2 import current_user
from schemas.requestUserSchema import userPydantic,user_marsh, update_userPydantic, update_user_marsh
from schemas.responseUserSchema import showUser
from marshmallow import ValidationError
router = APIRouter(
    tags = ['User']
)

@router.post('/user')
def add_user(data: userPydantic,cur_user: showUser = Depends(current_user)):
    try:
        data1 = dict(data)
        user_marsh().load(data1)
    except ValidationError as err:
        return err.messages
    return addUser.add_user(data,cur_user)

@router.get('/user',response_model = List[showUser])
def list_user(cur_user: showUser = Depends(current_user)):
    return listUser.list_user(cur_user)

@router.get('/user/{id}',response_model = showUser)
def list_user_id(id: int,cur_user: showUser = Depends(current_user)):
    return listUser.list_user_id(id,cur_user)

@router.put('/user/{id}')
def update_user(id: int,data: update_userPydantic,cur_user: showUser = Depends(current_user)):
    try:
        data1 = dict(data)
        update_user_marsh().load(data1)
    except ValidationError as err:
        return err.messages
    return updateUser.update_user(id,data,cur_user) 

@router.get('/supervisor',response_model = List[showUser])
def get_supervisors(cur_user: showUser = Depends(current_user)):
    return listSupervisor.supervisor_list(cur_user)

@router.delete('/user/{id}')
def delete_user(id: int,cur_user: showUser = Depends(current_user)):
    return deleteUser.users_delete(cur_user,id)