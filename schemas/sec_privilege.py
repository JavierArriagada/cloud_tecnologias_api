from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sec_privilege(Base):
    id: Optional[int]
    id_resource: int
    id_userole: int
    privtype: str