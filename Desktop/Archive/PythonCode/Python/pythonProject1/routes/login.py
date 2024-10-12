from datetime import datetime
from datetime import timedelta
from typing import Union

from fastapi import APIRouter, Response, status, HTTPException, Depends, Header, Request
from passlib.context import CryptContext
from pyasn1.compat import string
from starlette.responses import JSONResponse

from config.db import db
from models.check_data import is_blank
from jose import JWTError, jwt
import requests
import os


login_router = APIRouter()
DB = db()["users"]
SECRET_KEY = "jwt_key"
ALGORITHM = "HS256"


def __validate(req: dict):
    if req.get("email") is None or is_blank(req.get("email")) is True:
        return False, "email cannot be null"
    if req.get("password") is None or is_blank(req.get("password")) is True:
        return False, "password cannot be null"
    return req, ""


def __hash_password(pwd: str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(pwd)


def __verify_password(password: str, hashed_password: str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    result = pwd_context.verify(password, hashed_password)
    if result is not True:
        return False, f"password is not correct"
    return True, ""


def __active_user(status: str):
    if status != "yes":
        return False, f"your account has not activated, please activate your account"
    return True, f"your account has been activated"


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


@login_router.post('/users/login', status_code=201)
def login(req: dict, response: Response):
    # check input require
    is_ok, msg = __validate(req)
    if is_ok is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return msg
    # check email
    user = DB.find_one({'email': req["email"]})
    if user is None:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return f"email invalid"
    # check password
    ok, msg = __verify_password(req["password"], user["password"])
    if ok is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return msg
    # check active
    activated, txt = __active_user(user["verified"])
    if activated is False:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return txt
    # create access token
    access_token_expires = timedelta(seconds=30)
    access_token = create_access_token(
        data={"email": user["email"], "name": user["name"]}, expires_delta=access_token_expires
    )
    # Store access tokens in cookie
    response.set_cookie('access_token', access_token, 10, 10
                        , '/', None, False, True, 'lax')
    return {"access_token": access_token}


@login_router.post('/users/login/refresh', status_code=201)
def create_refresh_token(response: Response, request: Request):
    # get token
    token_bearer = request.headers.get('Authorization')
    token_array = str.split(token_bearer)
    if len(token_array) != 2:
        return f"token invalid"
    token = token_array[1]
    # decode token
    tkn = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    if tkn.get("email") is None or tkn.get("name") is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return f"token invalid"
    # create refresh token
    fresh_token_expires = timedelta(days=7)
    fresh_token = create_access_token(
        data={"email": tkn["email"], "name": tkn["name"]}, expires_delta=fresh_token_expires
    )
    # Store refresh and access tokens in cookie
    response.set_cookie('fresh_token', fresh_token, 7, 7
                        , '/', None, False, True, 'lax')
    return {"refresh_token": fresh_token}

