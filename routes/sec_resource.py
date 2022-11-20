from fastapi import APIRouter, Response, status
from config.db import conn

"""

from models.sec_resource import sec_resources


"""
from models.sec_resource import SecResource

from schemas.sec_resource import Sec_resource
from starlette.status import HTTP_204_NO_CONTENT

sec_resource = APIRouter()

@sec_resource.get("/sec_resource", response_model=list[Sec_resource], tags=["sec_resource"])
def get_sec_resources():
    return conn.execute(SecResource.select()).fetchall()

@sec_resource.post("/sec_resource", response_model=Sec_resource, tags=["sec_resource"])
def create_sec_resource(sec_resource:Sec_resource):
    
    new_sec_resource = {
        "company": sec_resource.company,
        "name": sec_resource.name,
        "descrip": sec_resource.descrip,
        "creatdate": sec_resource.creatdate,
        "status": sec_resource.status
    }
    result = conn.execute(SecResource.insert().values(new_sec_resource))
    
    print(result.lastrowid)
    return conn.execute(SecResource.select().where(SecResource.c.id== result.lastrowid)).first()

@sec_resource.get("/sec_resource/{id}", response_model=Sec_resource, tags=["sec_resource"])
def get_sec_resource(id: int):
    return conn.execute(SecResource.select().where(SecResource.c.id== id)).first()

@sec_resource.delete("/sec_resource/{id}", status_code=HTTP_204_NO_CONTENT, tags=["sec_resource"]  )
def delete_sec_resource(id: int):
    conn.execute(SecResource.delete().where(SecResource.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@sec_resource.put("/sec_resource/{id}", response_model=Sec_resource, tags=["sec_resource"])
def update_sec_resource(id: int, sec_resource : Sec_resource):
    
    update_sec_resource = {
        "company": sec_resource.company,
        "name": sec_resource.name,
        "descrip": sec_resource.descrip,
        "creatdate": sec_resource.creatdate,
        "status": sec_resource.status
    }
    
    conn.execute(SecResource.update().values(update_sec_resource).where(SecResource.c.id == id))
    return "updated"