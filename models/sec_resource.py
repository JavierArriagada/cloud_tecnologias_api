from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, SmallInteger, String, DateTime
from config.db import meta, engine

sec_resources = Table("sec_resource", meta, 
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("company", SmallInteger, nullable=False),
                    Column("name", String(100), nullable=False, unique=True),
                    Column("descrip", String(255), nullable=False),
                    Column("creatdate", DateTime(), nullable=False),
                    Column("status", String(1), nullable=False)                  
                    )

meta.create_all(engine)