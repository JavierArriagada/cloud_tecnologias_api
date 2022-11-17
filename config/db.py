from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Kj6mcacakk4fkd!@localhost:3306/cloud_tecnologias_api")

meta = MetaData()

conn = engine.connect()