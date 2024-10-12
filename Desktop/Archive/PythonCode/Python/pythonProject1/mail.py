# import os
# import template as template
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
# from starlette.responses import JSONResponse
# from pydantic import EmailStr, BaseModel
# from typing import List
# from dotenv import load_dotenv
# load_dotenv('.env')
#
#
# class Envs:
#     MAIL_USERNAME = os.getenv('MAIL_USERNAME')
#     MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
#     MAIL_FROM = os.getenv('MAIL_FROM')
#     MAIL_PORT = os.getenv('MAIL_PORT')
#     MAIL_SERVER = os.getenv('MAIL_SERVER')
#     MAIL_FROM_NAME = os.getenv('MAIN_FROM_NAME')
#
#
# class EmailSchema(BaseModel):
#    email: List[EmailStr]
#
#
# async def send_mail(subject, recipients, code: int):
#     conf = ConnectionConfig(
#         MAIL_USERNAME=Envs.MAIL_USERNAME,
#         MAIL_PASSWORD=Envs.MAIL_PASSWORD,
#         MAIL_FROM=Envs.MAIL_FROM,
#         MAIL_PORT=Envs.MAIL_PORT,
#         MAIL_SERVER=Envs.MAIL_SERVER,
#         MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
#         MAIL_TLS=True,
#         MAIL_SSL=False,
#     )
#
#     message = MessageSchema(
#         subject=subject,
#         recipients=recipients,
#         body=template,
#         subtype="html"
#     )
#     fm = FastMail(conf)
#     await fm.send_message(message)
#
#
#
