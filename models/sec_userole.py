"""from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, SmallInteger, String
from config.db import meta, engine
"""

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

from config.db import meta, engine

Base = declarative_base()
metadata = Base.metadata

class SecUserole(Base):
    __tablename__ = 'sec_userole'

    id = Column(INTEGER(11), primary_key=True)
    company = Column(SMALLINT(6), nullable=False)
    name = Column(String(40), nullable=False)
    lastname = Column(String(40), nullable=False)
    userlogin = Column(String(40), nullable=False)
    code = Column(String(20), nullable=False)
    usrpassword = Column(String(40), nullable=False)
    email = Column(String(100), nullable=False)






"""

sec_useroles = Table("sec_userole", meta, 
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("company", SmallInteger, nullable=False),
                    Column("name", String(40), nullable=False),
                    Column("lastname", String(40), nullable=False),
                    Column("userlogin", String(40), nullable=False),
                    Column("code", String(20), nullable=False),
                    Column("usrpassword", String(40), nullable=False),
                    Column("email", String(100), nullable=False)                    
                    )
"""


metadata.create_all(engine)