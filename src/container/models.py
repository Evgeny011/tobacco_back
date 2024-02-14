from sqlalchemy import Column, Integer, TIMESTAMP, String

from src.base import Base

from sqlalchemy.sql import func

from sqlalchemy.orm import validates

from pydantic import BaseModel, Field


class Container(Base):
    __tablename__ = 'Containers'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)
    weight = Column(Integer)
    timestamp = Column(TIMESTAMP, server_default = func.current_timestamp())

    @validates('weight')
    def validate_value(self, key, weight):
        if weight <= 0:
            raise ValueError("Weight container must be greater than 0")
        return weight


class  ContainerInput(BaseModel):
    name: str = Field(min_length = 1, max_length = 40)
    weight: int = Field(gt=1, lt=251)