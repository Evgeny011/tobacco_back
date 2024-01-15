from fastapi import APIRouter

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from queries.models import  Inventory

from datetime import datetime


inventory_router = APIRouter(tags=['Create Inventory'], prefix='/inventory')
engine = create_engine('sqlite:///database.sqlite', echo=True)
sessionLocal = sessionmaker(autoflush=True, bind=engine)


@inventory_router.post("/create")
async def create_inventory(start_date:str,end_date:str):
    db = sessionLocal()
    start_date_obj = datetime.strptime(start_date, '%d.%m.%Y').date()
    end_date_obj = datetime.strptime(end_date, '%d.%m.%Y').date()
    inventory = Inventory(start_date=start_date_obj, end_date=end_date_obj)
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory


