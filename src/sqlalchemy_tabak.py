import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import ForeignKey


engine = db.create_engine('sqlite:///database.sqlite', 
                          echo=True)

connection = engine.connect()
metadata = db.MetaData()
Inventories = db.Table('inventories', metadata,
                db.Column("id", db.Integer, autoincrement=True, primary_key=True),
                db.Column("start_date", db.Date),
                db.Column("end_date", db.Date),
                db.Column("timestamp", db.TIMESTAMP, server_default= db.func.current_timestamp())
)


weighings = db.Table('weighings',metadata,
                db.Column("id", db.Integer, autoincrement=True, primary_key=True),
                db.Column("value", db.Integer),
                db.Column("inventory_id", db.Integer, ForeignKey('inventories.id')),
                db.Column("timestamp", db.TIMESTAMP, server_default= db.func.current_timestamp())
)


containers = db.Table('containers', metadata,
                db.Column("id", db.Integer, autoincrement=True, primary_key=True),
                db.Column("name", db.String),
                db.Column("weight", db.Integer),
                db.Column("timestamp", db.TIMESTAMP, server_default= db.func.current_timestamp())
)

metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine) #Вероятно из-за этого чистит все нахуй

