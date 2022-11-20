"""from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger, String, DateTime
from config.db import meta, engine
from sqlalchemy.orm import  relationship
"""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER, STRING
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from config.db import meta, engine

Base = declarative_base()
metadata = Base.metadata



class SecPrivilege(Base):
    __tablename__ = 'sec_privilege'

    id = Column(INTEGER(11), primary_key=True)
    id_resource = Column(ForeignKey('sec_resource.id'), nullable=False, index=True)
    id_userole = Column(ForeignKey('sec_userole.id'), nullable=False, index=True)
    privtype = Column(String(1), nullable=False)

    sec_resource = relationship('SecResource')
    sec_userole = relationship('SecUserole')






"""




sec_privileges = Table("sec_privilege", meta,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("id_resource", ForeignKey('sec_resource.id'), nullable=False, index=True),
                    Column("id_userole", ForeignKey('sec_userole.id'), nullable=False, index=True),
                    Column("privtype", String(1),nullable=False),  
                    
                    sec_resource = relationship('Sec_resource'),
                    sec_userole = relationship('Sec_userole')              
                    )



"""

metadata.create_all(engine)