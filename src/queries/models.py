from sqlalchemy import Column, Integer, Date, TIMESTAMP, Sequence, ForeignKey, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.sql import func

from sqlalchemy.orm import validates, relationship

from pydantic import BaseModel


Base = declarative_base()

class Inventory(Base):
    __tablename__ = 'inventories'
    id = Column(Integer, primary_key = True, autoincrement = True)
    start_date = Column(Date)
    end_date = Column(Date)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())
    weighings = relationship("Weighing", back_populates="inventory", cascade="all, delete-orphan")

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


class Weighing(Base):
    __tablename__= 'weighings'
    id = Column(Integer, primary_key = True, autoincrement = True)
    value = Column(Integer)
    inventory_id = Column(Integer,  ForeignKey('inventories.id'))
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())
    inventory = relationship("Inventory", back_populates="weighings")

    @validates('value')
    def validate_value(self, key, value):
        if value <= 0:
            raise ValueError("Weight value must be greater than 0")
        return value


class Container(Base):
    __tablename__ = 'Containers'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)
    weight = Column(Integer)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())


class  ContainerInput(BaseModel):
    name: str
    weight: int

class InventoryInput(BaseModel):
    start_date: str
    end_date: str

class WeighingInput(BaseModel):
    inventory_id: int
    value: int
    container_count: int
    container_id: int

