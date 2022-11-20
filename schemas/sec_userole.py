from typing import Optional
from pydantic import BaseModel

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sec_userole(Base):
    id: Optional[int]
    company: int
    name: str
    lastname: str
    userlogin: str
    code: str
    usrpassword: str
    email: str