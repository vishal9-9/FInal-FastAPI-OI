from pydantic import BaseModel
from typing import Optional
from marshmallow import Schema,fields

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
    company_name = fields.String(required = True)
    country= fields.String(required = True)
    state= fields.String(required = True)
    city= fields.String(required = True)
    pincode= fields.String(required = True)
    department= fields.String(required = True)
    branch= fields.String(required = True)
    address= fields.String(required = True)