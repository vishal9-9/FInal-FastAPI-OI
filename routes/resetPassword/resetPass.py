from fastapi import APIRouter
from schemas import resetPass
from marshmallow import ValidationError
from resetPassword import resetPasswords

router = APIRouter(
    tags = ['Reset Password']
)

@router.post('/resetpassword')
async def reset_pass(request: resetPass.resetPassPydantic):
    try:
        requests = dict(request)
        resetPass.resetPassMarsh().load(requests)
    except ValidationError as err:
        return err.messages
    return await resetPasswords.reset_password(request)