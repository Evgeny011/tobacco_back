from sqlalchemy import Column, Integer, Date, TIMESTAMP

from src.base import Base

from sqlalchemy.sql import func

from sqlalchemy.orm import validates, relationship

from pydantic import BaseModel


class Inventory(Base):
    __tablename__ = 'inventories'
    id = Column(Integer, primary_key = True, autoincrement = True)
    start_date = Column(Date)
    end_date = Column(Date)
    timestamp = Column(TIMESTAMP, server_default = func.current_timestamp())
    
    weighings = relationship("Weighing", backref = "inventory", cascade = "all, delete-orphan")

    @validates('start_date')
    def validate_start_date(self, key, start_date):
        if self.end_date and start_date:
            if start_date >= self.end_date:
                raise ValueError('Start date must be less than end date')
        return start_date

    @validates('end_date')
    def validate_end_date(self, key, end_date):
        if self.start_date and end_date:
            if end_date <= self.start_date:
                raise ValueError('End date must be greater than start date')
        return end_date

class InventoryInput(BaseModel):
    start_date: str
    end_date: str