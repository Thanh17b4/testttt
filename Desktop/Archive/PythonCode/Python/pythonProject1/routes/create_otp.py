import random
import ssl
from datetime import timedelta, datetime
from starlette import status
from starlette.responses import JSONResponse
import smtplib
from config.db import user_otp, users
from fastapi import APIRouter, Response
from schemas.schemas import CreateOTPRequest
user_otp_router = APIRouter()


@user_otp_router.post('/users/create/otp')
def create_user_otp(req: CreateOTPRequest, response: Response):
    email = req.lock().get("email")
    user = users.find_one({"email": email})
    if user is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"email is not correct"
    user_id = user.get("_id")
    user_name = user.get("name")
    # create OTP
    OTP = random.randint(100000, 999999)
    created_at = datetime.now()
    expired_at = created_at + timedelta(minutes=5)
    user_otp_dict = {'user_id': user_id, 'OTP': OTP, 'created_at': created_at, 'expired_at': expired_at}
    user_otp_object = user_otp.insert_one(user_otp_dict)
    print(user_otp_object)
    # send email
    sender = "thanhpv@vmodev.com"
    receiver = "thanhpham.hvnh@gmail.com"
    subject = "to send email for testing"
    text = f"hello Mr/Mrs {user_name}, here is your OTP: {OTP}"
    message = 'Subject: {}\n\n{}'.format(subject, text)
    __send_email(sender, receiver, message)
    return JSONResponse(status_code=200, content={"message": "OTP had been sent to your email"})


def __send_email(sender: str, receiver: str, message: str):
    context = ssl.create_default_context()  # Create a secure SSL context
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls(context=context)  # Secure the connection
        s.login("thanhpv@vmodev.com", "yenqoepplszlvaqw")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    s.sendmail(sender, receiver, message)
    s.quit()