from fastapi import APIRouter

from sqlalchemy.orm import sessionmaker, validates
from sqlalchemy import create_engine

from queries.models import  Inventory

from datetime import datetime

from pydantic import BaseModel




inventory_router = APIRouter(tags=['Create Inventory'], prefix='/inventory')
engine = create_engine('sqlite:///database.sqlite', echo=True)
sessionLocal = sessionmaker(autoflush=True, bind=engine)

class InventoryInput(BaseModel):
    start_date: str
    end_date: str

@inventory_router.post("/create")
async def create_inventory(data: InventoryInput):
    db = sessionLocal()
    start_date_obj = datetime.strptime(data.start_date, '%d.%m.%Y').date()
    end_date_obj = datetime.strptime(data.end_date, '%d.%m.%Y').date()
    inventory = Inventory(start_date=start_date_obj, end_date=end_date_obj)
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory

@inventory_router.delete("/delete/{id}")
async def delete_inventory_by_id(id: int):
    db = sessionLocal()
    inventory = db.query(Inventory).filter(Inventory.id == id).first()
    if inventory:
        db.delete(inventory)
        db.commit()
        return {"message": "The inventory was successfully deleted"}
    else:
        return {"error": "Inventory was not deleted"}

@inventory_router.get("/get")
async def get_inventories():
    db = sessionLocal()
    inventory = db.query(Inventory).all()
    return inventory

@inventory_router.get("/get/{id}")
async def get_inventory_by_id(id: int):
    db = sessionLocal()
    inventory = db.query(Inventory).filter(Inventory.id == id).first()
    return inventory

