from fastapi import FastAPI
from routes.sec_userole import sec_userole
from routes.sec_resource import sec_resource
from routes.sec_privilege import sec_privilege

app = FastAPI()

app.include_router(sec_userole)
app.include_router(sec_resource)
app.include_router(sec_privilege)