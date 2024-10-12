from datetime import datetime

from jose import jwt

from jwt_user.author import request_token, verify_token, ALGORITHM
from bson import ObjectId
from fastapi import APIRouter, Response, Request
from passlib.context import CryptContext
from starlette import status
from models.check_data import is_blank
from result_return.user import user_result
from routes.login import SECRET_KEY
from schemas.schemas import User
from config.db import db


user_router = APIRouter()
DB = db()["users"]


@user_router.post('/users/create')
def create_user(request: User, response: Response):
    user = request.user_to_dict()
    print(user)
    # Validate data
    is_ok, msg = __validate(user)
    if is_ok is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return msg
    # check and hash password
    hash_password = __hash_password(user.get("password"))
    created_at = datetime.now()
    updated_at = datetime.now()
    user.update({"password": hash_password, "created_at": created_at, "updated_at": updated_at})
    # check if require filed is unique
    if DB.find_one({"email": user["email"]}) is not None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f"email had been used"
    new_user = DB.insert_one(user)
    response.status_code = status.HTTP_201_CREATED
    return f"customer_id {new_user.inserted_id} has been inserted successfully"


def __validate(req: dict):
    if req.get("name") is None or is_blank(req.get("name")) is True:
        return False, "name cannot be null"
    if req.get("email") is None or is_blank(req.get("email")) is True:
        return False, "email cannot be null"
    if req.get("role") is None or is_blank(req.get("role")) is True:
        return False, "role cannot be null"
    if req.get("verified") is None or is_blank(req.get("verified")) is True:
        return False, "verified cannot be null"
    if req.get("password") is None or is_blank(req.get("password")) is True:
        return False, "password cannot be null"
    return req, ""


def __hash_password(pwd: str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return True, pwd_context.hash(pwd)


@user_router.get('/users/detail/{id}', tags=["users"])
def detail_user(id: str, response: Response, req: Request):
    # request token
    token, err = request_token(req)
    if token is False:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return err
    decode_token = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    email = decode_token.get("email")
    is_ok, msg = __check_length_id(id)
    if is_ok is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return msg
    user = DB.find_one({'_id': ObjectId(str(id))})
    if user is None:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return f"user_ID is not correct"
    if user.get("email") != email:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return f"user_id invalid"
    response.status_code = status.HTTP_200_OK
    return {"status": "success", "user": user_result(user)}


def __check_length_id(req: str):
    if len(req) != 24:
        return False, f"user_ID is {len(req)} characters is not correct, it must include 24 characters"
    return req, ""
