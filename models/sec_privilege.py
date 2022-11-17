from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger, String, DateTime
from config.db import meta, engine
from sqlalchemy.orm import  relationship


sec_privileges = Table("sec_privilege", meta,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("id_resource", ForeignKey('sec_resource.id'), nullable=False, index=True),
                    Column("id_userole", ForeignKey('sec_userole.id'), nullable=False, index=True),
                    Column("privtype", String(1),nullable=False),  
                    
                    sec_resource = relationship('Sec_resource'),
                    sec_userole = relationship('Sec_userole')              
                    )

meta.create_all(engine)

