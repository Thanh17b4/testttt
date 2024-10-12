from datetime import datetime
from starlette import status
from config.db import user_otp, users
from fastapi import APIRouter, Response
from models.check_data import is_blank, is_integer
from schemas.schemas import ActivateRequest
from result_return.user import user_result
activate_router = APIRouter()


@activate_router.put('/users/create/activate')
def activate_router_otp(request: ActivateRequest, response: Response):
    # Validate data
    req = request.lock()
    is_ok, msg = __validate(req)
    if is_ok is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return msg
    # check User which was existed or not
    User = users.find_one({"email": req["email"]})
    if User is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"email is not correct"
    # check User has been activated or not:
    stt = User.get("verified")
    if stt == "yes":
        return f"your account had been activated before"
    # check OTP
    user_id = User.get("_id")
    user_otp_object = user_otp.find({"user_id": user_id}).sort("created_at", -1).limit(1)
    for x in user_otp_object:
        if req["OTP"] != x.get("OTP"):
            return f"OTP is not correct"
        if datetime.now() > x.get("expired_at"):
            return f"OTP has expired"
    # activate account
    activated_user = users.update_one({"email": req["email"]}, {"$set": {"verified": "yes"}})
    return f"your account has been activated successfully, {activated_user.modified_count} documents updated."


def __validate(req: dict):

    if req.get("email") is None or is_blank(req.get("email")) is True:
        return False, "email cannot be null"
    if req.get("OTP") is None or is_integer(req.get("OTP")) is False:
        return False, "OTP cannot be null and must be number"

    return req, ""


