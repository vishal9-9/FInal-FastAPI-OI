from pydantic import BaseModel
from datetime import date

class showUser(BaseModel):
    id: int
    c_id: int
    fullname: str
    email: str
    contact_no: str
    working_under: int
    dob: date
    class Config:
        orm_mode = True