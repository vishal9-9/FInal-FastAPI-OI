from pydantic import BaseModel
from typing import Optional
from marshmallow import Schema,fields,validate

class company_pydantic(BaseModel):
    company_name: Optional[str]
    country: Optional[str]
    state: Optional[str]
    city: Optional[str]
    pincode: Optional[str]
    department: Optional[str]
    branch: Optional[str]
    address: Optional[str]

class company_marsh(Schema):
    company_name = fields.String(required = True,validate=validate.Length(min=3))
    country = fields.String(required = True,validate=validate.Length(min=5))
    state = fields.String(required = True,validate=validate.Length(min=3))
    city = fields.String(required = True,validate=validate.Length(min=3))
    pincode = fields.String(required = True,validate=[validate.Length(min=6,max=6),validate.Regexp(r'[0-9]',error='Please Enter Valid Pincode')])
    department = fields.String(required = True,validate=validate.Length(min=3))
    branch = fields.String(required = True,validate=validate.Length(min=3))
    address = fields.String(required = True,validate=validate.Length(min=10))