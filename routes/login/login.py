from fastapi import APIRouter
from login import login
from marshmallow import ValidationError
from schemas import loginSchema

router = APIRouter(
    tags = ['Login']
)

@router.post('/login')
def auth(request: loginSchema.loginPydantic):
    try:
        requests = dict(request)
        loginSchema.request_login().load(requests)
    except ValidationError as err:
        return err.messages
    return login.login_user(request)