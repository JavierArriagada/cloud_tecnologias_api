from typing import Optional
from pydantic import BaseModel

class Sec_userole(BaseModel):
    id: Optional[int]
    company: int
    name: str
    lastname: str
    userlogin: str
    code: str
    usrpassword: str
    email: str