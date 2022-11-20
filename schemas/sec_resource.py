from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sec_resource(Base):
    id: Optional[int]
    company: int
    name: str
    descrip: str
    creatdate: datetime
    status: str