from sqlalchemy import Column, Integer, Date, TIMESTAMP

from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Inventory(Base):
    __tablename__ = 'Inventories'
    ID = Column(Integer, primary_key=True)
    Start_Date = Column(Date)
    End_Date = Column(Date)
    Timestamp = Column(TIMESTAMP)

    