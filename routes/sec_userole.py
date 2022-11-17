from fastapi import APIRouter, Response, status
from config.db import conn
from models.sec_userole import sec_useroles
from models.sec_privilege import sec_privileges
from models.sec_resource import sec_resources

from schemas.sec_userole import Sec_userole
from schemas.sec_privilege import Sec_privilege
from schemas.sec_resource import Sec_resource

from starlette.status import HTTP_204_NO_CONTENT

sec_userole = APIRouter()

@sec_userole.get("/sec_userole", response_model=list[Sec_userole], tags=["sec_userole"])
def get_sec_useroles():
    return conn.execute(sec_useroles.select()).fetchall()

@sec_userole.post("/sec_userole", response_model=Sec_userole, tags=["sec_userole"])
def create_sec_userole(sec_userole:Sec_userole):
    
    new_sec_userole = {
        "company": sec_userole.company,
        "name": sec_userole.name,
        "lastname": sec_userole.lastname,
        "userlogin": sec_userole.userlogin,
        "code": sec_userole.code,
        "usrpassword": sec_userole.usrpassword,
        "email": sec_userole.email
    }
    result = conn.execute(sec_useroles.insert().values(new_sec_userole))
    
    #print(result.lastrowid)
    return conn.execute(sec_useroles.select().where(sec_useroles.c.id == result.lastrowid)).first()

@sec_userole.get("/sec_userole/{id}", response_model=Sec_userole, tags=["sec_userole"])
def get_sec_userole(id: int):
    return conn.execute(sec_useroles.select().where(sec_useroles.c.id== id)).first()

@sec_userole.delete("/sec_userole/{id}", status_code=HTTP_204_NO_CONTENT, tags=["sec_userole"]  )
def delete_sec_userole(id: int):
    conn.execute(sec_useroles.delete().where(sec_useroles.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@sec_userole.put("/sec_userole/{id}", response_model=Sec_userole, tags=["sec_userole"])
def update_sec_userole(id: int, sec_userole : Sec_userole):
    
    update_sec_userole = {
        "company": sec_userole.company,
        "name": sec_userole.name,
        "lastname": sec_userole.lastname,
        "userlogin": sec_userole.userlogin,
        "code": sec_userole.code,
        "usrpassword": sec_userole.usrpassword,
        "email": sec_userole.email
    }
    
    conn.execute(sec_useroles.update().values(update_sec_userole).where(sec_useroles.c.id == id))
    return "updated"



@sec_userole.put("/sec_userole/privilege/" ,tags=["sec_userole"])
def update_sec_userole( id: int , sec_privilege : Sec_privilege):
    
   # privilege = conn.execute(sec_privilege.select()).fetchall()
    
    
    update_sec_privilege = {
        "id": sec_privilege.id,
        "id_userole":sec_privilege.id_userole,
        "id_resource":sec_privilege.id_resource,
        "privtype": sec_privilege.privtype,
        
        
    }
   
   
   
    conn.execute(sec_privileges.update().values(update_sec_privilege).where(sec_privileges.c.id == id))
    return "updated"

'''
@sec_userole.put("/sec_userole/{sec_userole_id}/code/{sec_userole_code}", response_model=Sec_userole ,tags=["sec_userole"])
def update_sec_userole(sec_userole_id: int, sec_userole_code: str, sec_privilege_id: int , sec_privilege : Sec_privilege):
    
    update_sec_privilege = {
        
        "privtype": sec_privilege.privtype,
        
    }
   
   
    conn.execute(sec_privileges.update().values(update_sec_privilege).where(sec_privileges.c.id == sec_privilege_id  and sec_resources.c.id == sec_resource_id and sec_useroles.c.id == sec_userole_id))
    return "updated"
    '''
    
@sec_userole.delete("/sec_userole/{sec_userole_id}/sec_resource/{sec_resource_id}" ,tags=["sec_userole"])
def delete_sec_privilege_by_sec_resource( sec_userole_id: int ,sec_resource_id: int, sec_privilege : Sec_privilege):
    
   # privilege = conn.execute(sec_privilege.select()).fetchall()
    conn.execute(sec_privileges.delete().where(sec_privileges.c.id_userole == sec_userole_id and sec_resources.c.id_resource == sec_resource_id ))
    return "deleted"
