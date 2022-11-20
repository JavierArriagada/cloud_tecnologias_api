"""from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, SmallInteger, String, DateTime
from config.db import meta, engine
"""

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

from config.db import meta, engine

Base = declarative_base()
metadata = Base.metadata

class SecResource(Base):
    __tablename__ = 'sec_resource'

    id = Column(INTEGER(11), primary_key=True)
    company = Column(SMALLINT(6), nullable=False)
    name = Column(String(100), nullable=False, unique=True)
    descrip = Column(String(255), nullable=False)
    creatdate = Column(DateTime, nullable=False)
    status = Column(String(1), nullable=False)






"""
sec_resources = Table("sec_resource", meta, 
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("company", SmallInteger, nullable=False),
                    Column("name", String(100), nullable=False, unique=True),
                    Column("descrip", String(255), nullable=False),
                    Column("creatdate", DateTime(), nullable=False),
                    Column("status", String(1), nullable=False)                  
                    )
"""


metadata.create_all(engine)