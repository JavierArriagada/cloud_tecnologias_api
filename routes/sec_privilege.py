from fastapi import APIRouter, Response
from config.db import conn

"""
from models.sec_privilege import sec_privileges
"""


from models.sec_privilege import SecPrivilege


from schemas.sec_privilege import Sec_privilege

from starlette.status import HTTP_204_NO_CONTENT

sec_privilege = APIRouter()

@sec_privilege.get("/sec_privilege", response_model=list[Sec_privilege], tags=["sec_privilege"])
def get_sec_privileges():
    return conn.execute(SecPrivilege.select()).fetchall()

@sec_privilege.post("/sec_privilege", response_model=Sec_privilege, tags=["sec_privilege"])
def create_sec_privilege(sec_privilege:Sec_privilege):
    
    new_sec_privilege = {
        "id_resource": sec_privilege.id_resource,
        "id_userole": sec_privilege.id_userole,
        "privtype": sec_privilege.privtype
    }
    result = conn.execute(SecPrivilege.insert().values(new_sec_privilege))
    
    print(result.lastrowid)
    return conn.execute(SecPrivilege.select().where(SecPrivilege.c.id== result.lastrowid)).first()

@sec_privilege.get("/sec_privilege/{id}", response_model=Sec_privilege, tags=["sec_privilege"])
def get_sec_privilege(id: int):
    return conn.execute(SecPrivilege.select().where(SecPrivilege.c.id== id)).first()

@sec_privilege.delete("/sec_privilege/{id}", status_code=HTTP_204_NO_CONTENT, tags=["sec_privilege"]  )
def delete_sec_privilege(id: int):
    conn.execute(SecPrivilege.delete().where(SecPrivilege.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@sec_privilege.put("/sec_privilege/{id}", response_model=Sec_privilege, tags=["sec_privilege"])
def update_sec_privilege(id: int, sec_privilege : Sec_privilege):
    
    update_sec_privilege = {
        "id_resource": sec_privilege.id_resource,
        "id_userole": sec_privilege.id_userole,
        "privtype": sec_privilege.privtype
    }
    
    conn.execute(SecPrivilege.update().values(update_sec_privilege).where(SecPrivilege  .c.id == id))
    return "updated"