from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, SmallInteger, String
from config.db import meta, engine

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

meta.create_all(engine)