from sqlalchemy import Column, Integer, TIMESTAMP,  ForeignKey

from src.base import Base

from sqlalchemy.sql import func

from sqlalchemy.orm import  relationship

from pydantic import BaseModel, Field


class Weighing(Base):
    __tablename__= 'weighings'
    id = Column(Integer, primary_key = True, autoincrement = True)
    value = Column(Integer)
    inventory_id = Column(Integer,  ForeignKey('inventories.id'))
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())

class WeighingInput(BaseModel):
    inventory_id: int
    value: int = Field(gt = 1, lt = 35001)
    container_count: int = Field(gt = 0, lt = 350)
    container_id: int

