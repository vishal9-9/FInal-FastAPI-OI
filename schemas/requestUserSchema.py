from typing import Optional
from marshmallow import Schema,fields
from pydantic import BaseModel

class userPydantic(BaseModel):
    c_id: Optional[int] 
    fullname: Optional[str]
    email: Optional[str]
    password: Optional[str]
    contact_no: Optional[str]
    working_under: Optional[int]
    dob: Optional[str]
    role_id: Optional[int]

class update_userPydantic(BaseModel):
    c_id: Optional[int]
    fullname: Optional[str]
    email: Optional[str]
    contact_no: Optional[str]
    working_under: Optional[int]
    dob: Optional[str]
    role_id: Optional[int]

class user_marsh(Schema):
    c_id = fields.Integer(required = True)
    fullname = fields.String(required = True)
    email = fields.Email(required = True)
    password = fields.String(required = True)
    contact_no = fields.String(required = True)
    working_under = fields.Integer(required = True)
    dob = fields.Date(required = True)
    role_id = fields.Integer(required = True)

class update_user_marsh(Schema):
    c_id = fields.Integer(required = True)
    fullname = fields.String(required = True)
    email = fields.Email(required = True)
    contact_no = fields.String(required = True)
    working_under = fields.Integer(required = True)
    dob = fields.Date(required = True)
    role_id = fields.Integer(required = True)
