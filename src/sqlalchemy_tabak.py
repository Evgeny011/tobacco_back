import sqlalchemy as db


engine = db.create_engine('sqlite:///Inventories-sqlalchemy.db', 
                          echo=True)
connection = engine.connect()
metadata = db.MetaData()
Inventories = db.Table('Inventories', metadata,
db.Column("ID", db.Integer),
db.Column("Start_Date", db.Date),
db.Column("End_Date", db.Date),
db.Column("Timestamp", db.TIMESTAMP)
)
metadata.create_all(engine)

