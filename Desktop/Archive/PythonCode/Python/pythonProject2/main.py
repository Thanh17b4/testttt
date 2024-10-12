from fastapi import FastAPI
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from starlette.requests import Request
from starlette.responses import JSONResponse, WebSocketException
from pydantic import EmailStr, BaseModel
from typing import List

app = FastAPI()


class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME='myGmailAddress',
    MAIL_PASSWORD="myPassword",
    MAIL_FROM='myGmailAddress',
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False
)


@app.post("/send_mail")
async def send_mail(email: Emai         lSchema):
    template = """
        <html>
        <body>


<p>Hi !!!
        <br>Thanks for using <b>fastapi mail</b>!!!</p>


        </body>
        </html>
        """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass
        body=template,
        subtype="html"
    )

    template = """
<p>Hi !!!
<br>Thanks for using <b>fastapi mail</b>!!!
</p>"""

    '''
    template = """
<p>Hi !!!
<br>Thanks for using <b>fastapi mail</b>!!!
</p>"""
    '''

    fm = FastMail(conf)
    await fm.send_message(message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})