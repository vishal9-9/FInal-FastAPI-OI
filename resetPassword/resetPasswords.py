from database import databaseHelper
from fastapi_mail import MessageSchema,ConnectionConfig,FastMail
from fastapi import HTTPException
from http import HTTPStatus
import random
import string
from helpers import passhash
from config import logError,password

async def reset_password(data):
    if not databaseHelper.if_user_exist(data.email):
        raise HTTPException(status_code = HTTPStatus.NOT_FOUND, detail = logError.EMAIL_NOT_FOUND)
    letters = string.ascii_lowercase   
    new_password = ''.join(random.choice(letters) for i in range(8))
    try:
        databaseHelper.reset_pass(new_password,data.email)
    except:
        raise HTTPException(status_code = HTTPStatus.BAD_REQUEST, detail = logError.PROCESSING_ERROR)
    email = data.email
    conf = ConnectionConfig(
    MAIL_USERNAME = "vishal@openspaceservices.com",
    MAIL_PASSWORD = password.password,
    MAIL_FROM = "vishal@openspaceservices.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="OI-Analytics",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
    )
    message = MessageSchema(
    subject = "Reset Password",
            recipients = email,
            body = f'New Password id {new_password}', 
        )
    fm = FastMail(conf)
    await fm.send_message(message)
    raise HTTPException(detail = 'Mail Sent', status_code = HTTPStatus.OK)