from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Sec_privilege(BaseModel):
    id: Optional[int]
    id_resource: int
    id_userole: int
    privtype: str