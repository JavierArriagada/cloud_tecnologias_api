from fastapi import APIRouter, Response, status
from config.db import conn

"""
from models.sec_userole import sec_userole
from models.sec_privilege import sec_privileges
from models.sec_resource import sec_resources
"""

from models.sec_userole import SecUserole
from models.sec_privilege import SecPrivilege
from models.sec_resource import SecResource

from schemas.sec_userole import Sec_userole
from schemas.sec_privilege import Sec_privilege
from schemas.sec_resource import Sec_resource

from fastapi.responses import JSONResponse

from starlette.status import HTTP_204_NO_CONTENT

sec_userole = APIRouter()

@sec_userole.get("/sec_userole", response_model=list[Sec_userole], tags=["sec_userole"])
def get_sec_userole():
    return conn.execute(SecUserole.select()).fetchall()

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
    result = conn.execute(SecUserole.insert().values(new_sec_userole))
    
    #print(result.lastrowid)
    return conn.execute(SecUserole.select().where(SecUserole.c.id == result.lastrowid)).first()

@sec_userole.get("/sec_userole/{id}", response_model=Sec_userole, tags=["sec_userole"])
def get_sec_userole(id: int):
    return conn.execute(SecUserole.select().where(SecUserole.c.id== id)).first()

@sec_userole.delete("/sec_userole/{id}", status_code=HTTP_204_NO_CONTENT, tags=["sec_userole"]  )
def delete_sec_userole(id: int):
    conn.execute(SecUserole.delete().where(SecUserole.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@sec_userole.put("/sec_userole/{id}", tags=["sec_userole"])
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
    
    conn.execute(SecUserole.update().values(update_sec_userole).where(SecUserole.c.id == id))
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
   
   
   
    conn.execute(SecPrivilege.update().values(update_sec_privilege).where(SecPrivilege.c.id == id))
    return "updated"


    
@sec_userole.delete("/sec_userole/{sec_userole_id}/sec_resource/{sec_resource_id}" ,tags=["sec_userole"])
def delete_sec_privilege_by_sec_resource( sec_userole_id: int ,sec_resource_id: int):
    
   # privilege = conn.execute(sec_privilege.select()).fetchall()
    conn.execute(SecPrivilege.delete().where(SecPrivilege.c.id_userole == sec_userole_id and SecPrivilege.c.id_resource == sec_resource_id ))
   
    return "deleted"
    #return Response(status_code=HTTP_204_NO_CONTENT)




    
@sec_userole.patch("/update_sec_privilege/sec_userole/{sec_userole_id}/sec_resource/{sec_resource_id}/sec_privilege/{sec_privilege_id}/privtype/{privtype}", response_model=Sec_privilege ,tags=["sec_userole"])
def update_privilege( sec_userole_id: int ,sec_resource_id: int, sec_privilege_id: int, privtype : str  ):
    
    update_sec_privilege = {
        "privtype": privtype ,
                
    }
    
   
    
    #conn.execute(SecPrivilege.update().values(update_sec_privilege).where(SecPrivilege.c.id == sec_privilege_id and SecPrivilege.c.id_userole == sec_userole_id and SecPrivilege.c.id_resource == sec_resource_id))
   
    
    return  conn.execute(SecPrivilege.update().values(update_sec_privilege).where(SecPrivilege.c.id == sec_privilege_id and SecPrivilege.c.id_userole == sec_userole_id and SecPrivilege.c.id_resource == sec_resource_id))



@sec_userole.get("/sec_userole/code/{sec_userole_code}", response_model=list[Sec_privilege],  tags=["sec_userole"])
def get_privilege_by_sec_userole_code(sec_userole_code: str):
    result = conn.execute(SecUserole.select().where(SecUserole.c.code == sec_userole_code)).fetchall()
    
    
    #print(result[0][0])
    
   # priv = conn.execute(SecPrivilege.select().where(SecPrivilege.c.id_userole == result[0][0])).fetchall()
    
    #print(priv)
    
    return conn.execute(SecPrivilege.select().where(SecPrivilege.c.id_userole == result[0][0])).fetchall()

