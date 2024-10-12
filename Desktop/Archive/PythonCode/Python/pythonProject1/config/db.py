from pydantic import BaseSettings, EmailStr
from pymongo import MongoClient


def db():
    client = MongoClient("mongodb://localhost:27017/")
    mongoDB = client["mongoDB"]
    return mongoDB


users = db()["users"]
user_otp = db()["user_otp"]
