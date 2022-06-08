import imp
from marshmallow import fields,Schema
from pydantic import BaseModel
from typing import Optional

class loginPydantic(BaseModel):
    email: Optional[str]
    password: Optional[str]

class request_login(Schema):
    email = fields.Email(required = True)
    password = fields.String(required = True)