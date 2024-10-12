import time

import uvicorn
from fastapi import FastAPI
from routes.customer import customers_router
from routes.user import user_router
from routes.login import login_router
from routes.create_otp import user_otp_router
from routes.activate import activate_router
app = FastAPI()
app.include_router(customers_router)
app.include_router(user_router)
app.include_router(login_router)
app.include_router(user_otp_router)
app.include_router(activate_router)
uvicorn.run(app, host="localhost", port=8000)

