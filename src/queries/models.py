from sqlalchemy import Column, Integer, Date, TIMESTAMP

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.sql import func

Base = declarative_base()

class Inventory(Base):
    __tablename__ = 'inventories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date)
    end_date = Column(Date)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())
