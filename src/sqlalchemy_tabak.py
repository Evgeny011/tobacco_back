import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from queries.models import Inventory



engine = db.create_engine('sqlite:///database-sqlalchemy.db', 
                          echo=True)
connection = engine.connect()
metadata = db.MetaData()
Inventories = db.Table('inventories', metadata,
                db.Column("id", db.Integer, autoincrement=True),
                db.Column("start_date", db.Date),
                db.Column("end_date", db.Date),
                db.Column("timestamp", db.TIMESTAMP, server_default= db.func.current_timestamp())
)
metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)






