import sqlalchemy as db


engine = db.create_engine('sqlite:///Inventories-sqlalchemy.db', echo=True)
connection = engine.connect()
metadata = db.MetaData()
Inventories = db.Table('Inventories', metadata,
db.Column("ID", db.Integer),
db.Column("From", db.Date),
db.Column("To", db.Date),
db.Column("Timestamp", db.TIMESTAMP)
)
metadata.create_all(engine)
