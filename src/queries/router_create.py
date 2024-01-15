from fastapi import APIRouter


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel
from queries.models import  Inventory
 
Create_Inventory_rout = APIRouter(tags=['Create Inventory'], prefix='/create')
engine = create_engine('sqlite:///database-sqlalchemy.db', echo=True)
SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)


@Create_Inventory_rout.post("/")
async def create_inventory(start_date:str,end_date:str):
    db = SessionLocal()
    inventory = Inventory(start_date=start_date, end_date=end_date)
    db.add(inventory)
    db.commit()
    db.refresh(inventory,exclude_unset=True)
    return inventory


