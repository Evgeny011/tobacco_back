from fastapi import APIRouter

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel
from queries.models import  Inventory

from datetime import datetime


Create_Inventory_rout = APIRouter(tags=['Create Inventory'], prefix='/create')
engine = create_engine('sqlite:///database.sqlite', echo=True)
SessionLocal = sessionmaker(autoflush=True, bind=engine)


@Create_Inventory_rout.post("/")
async def create_inventory(start_date:str,end_date:str):
    db = SessionLocal()
    start_date_obj = datetime.strptime(start_date, '%d-%m-%Y').date()
    end_date_obj = datetime.strptime(end_date, '%d-%m-%Y').date()
    inventory = Inventory(start_date=start_date_obj, end_date=end_date_obj)
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory


