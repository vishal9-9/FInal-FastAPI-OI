from pydantic import BaseModel

class company_pydantic(BaseModel):
    company_name: str
    country: str
    state: str
    city: str
    pincode: str
    department: str
    branch: str
    address: str
    class Config:
        orm_mode = True