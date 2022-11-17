from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Sec_resource(BaseModel):
    id: Optional[int]
    company: int
    name: str
    descrip: str
    creatdate: datetime
    status: str