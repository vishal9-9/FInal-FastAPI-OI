from pydantic import BaseModel
from typing import Optional, List
from marshmallow import Schema,fields

class resetPassPydantic(BaseModel):
    email: List[Optional[str]]

class resetPassMarsh(Schema):
    email = fields.List(fields.Email(required = True))