from __future__ import annotations

from datetime import datetime


from pydantic import BaseModel, constr


class User(BaseModel):
    name: str
    email: str
    role: str
    verified: str = "No"
    password: constr(min_length=8)
    created_at: datetime or None = None
    updated_at: datetime or None = None

    def user_to_dict(self):
        return vars(self)


class ActivateRequest(BaseModel):
    email: str
    OTP: int

    def lock(self):
        return vars(self)


class CreateOTPRequest(BaseModel):
    email: str

    def lock(self):
        return vars(self)


class UserOtp(object):
    def __init__(self, data: dict):
        self.user_id = data["user_id"]
        self.OTP = data["OTP"]

    def otp_to_dict(self):
        return vars(self)


class Customer(object):
    # allowed_properties = ["=_id", "name", "address"]
    def __init__(self, data: dict):
        self._id = data["_id"]
        self.name = data["name"]
        # Method 1
        # if data.get("address") is not None:
        self.address = data["address"]
        self.password = data["password"]

    def to_dict(self):
        return vars(self)


# class User(object):
#     def __init__(self, data: dict):
#         # self._id = data["_id"]
#         self.name = data["name"]
#         self.email = data["email"]
#         self.role = data["role"]
#         self.verified = data["verified"]
#         self.password = data["password"]
#
#     def user_to_dict(self):
#         return vars(self)