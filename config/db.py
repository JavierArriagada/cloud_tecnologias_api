from sqlalchemy import create_engine, MetaData


engine = create_engine("sqlite:///sqlite3.db")

meta = MetaData()

conn = engine.connect()