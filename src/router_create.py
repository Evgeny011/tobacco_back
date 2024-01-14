from fastapi import FastAPI
from fastapi import APIRouter


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.queries.models import  Inventory  #Base


Create_Inventory_rout = APIRouter(tags = ['Create Inventory'], prefix = 'create')



engine = create_engine('sqlite:///Inventories-sqlalchemy.db', echo = True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@Create_Inventory_rout.post("/")
async def create_inventory(start_date: str, end_date: str, timestamp: str):
    db = SessionLocal()
    inventory = Inventory(Start_Date=start_date, End_Date=end_date, Timestamp=timestamp)
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory