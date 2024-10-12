from datetime import datetime, timedelta
from fastapi import Request
from jose import jwt
SECRET_KEY = "jwt_key"
ALGORITHM = "HS256"
# from config.db import db
# verify_router = APIRouter()
# DB = db()["users"]


def __check_expire(unix_time: int):
    date_format_str = '%Y-%m-%d %H:%M:%S'
    convert_unix_to_str = (datetime.fromtimestamp(unix_time)).strftime(date_format_str)
    convert_unix_to_date = datetime.strptime(convert_unix_to_str, date_format_str)
    want_time_date = convert_unix_to_date + timedelta(seconds=30)
    time_now_str = datetime.now().strftime(date_format_str)
    time_now_date = datetime.strptime(time_now_str, date_format_str)
    if time_now_date > want_time_date:
        return False, "time is over"
    return True, ""


def verify_token(token: str):
    decode_token = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    if decode_token.get("email") is None or decode_token.get("name") is None:
        return False, f"token invalid"
    boolean, msg = __check_expire(decode_token.get("exp"))
    if boolean is False:
        return False, msg
    return True, ""


def request_token(request: Request):
    token_bearer = request.headers.get('Authorization')
    token_array = str.split(token_bearer)
    if len(token_array) != 2:
        return None, f"token invalid"
    token = token_array[1]
    ok, txt = verify_token(token)
    if ok is False:
        return None, txt
    return token, ""





