from fastapi import APIRouter,Depends
from typing import List
from schemas.responseUserSchema import showUser
from schemas.requestCompanySchema import company_marsh,company_pydantic
from login.oauth2 import current_user
from marshmallow import ValidationError
from manageCompany import addCompany,listCompany,updateCompany,deleteCompany
from schemas import responseCompanySchema

router = APIRouter(
    tags = ['Company']
)

@router.post('/company')
def add_new_company(data: company_pydantic,cur_user: showUser = Depends(current_user)):
    try:
        data1 = dict(data)
        company_marsh().load(data1)
    except ValidationError as err:
        return err.messages
    return addCompany.add_new_company(data,cur_user)

@router.get('/company',response_model = List[responseCompanySchema.company_pydantic])
def get_company(cur_user: showUser = Depends(current_user)):
    return listCompany.list_of_company(cur_user)

@router.get('/company/{id}',response_model = responseCompanySchema.company_pydantic)
def get_company_details(id: int,cur_user: showUser = Depends(current_user)):
    return listCompany.list_of_company_id(cur_user,id)

@router.put('/company/{id}')
def add_new_company(id: int,data: company_pydantic,cur_user: showUser = Depends(current_user)):
    try:
        data1 = dict(data)
        company_marsh().load(data1)
    except ValidationError as err:
        return err.messages
    return updateCompany.update_company(data,cur_user,id)

@router.delete('/company/{id}')
def delete_company(id: int,cur_user: showUser = Depends(current_user)):
    return deleteCompany.del_company(cur_user,id)
