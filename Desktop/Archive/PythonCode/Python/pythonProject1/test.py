from datetime import datetime

import self as self
from bson import ObjectId
from pydantic import BaseModel
from requests import Response
from starlette import status

from config.db import user_otp, users
from models.check_data import is_blank, is_integer
from schemas.schemas import ActivateRequest


if __name__ == '__main__':
    class CustomerTest(BaseModel):
        _id: int
        name: str
        address: str
        password: str

    def test(a: CustomerTest):
        return a
    m = CustomerTest()
    b = test(m)

    print(b)