from fastapi import APIRouter, HTTPException

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from src.queries.models import Weighing, Inventory, Container

from src.queries.models import WeighingInput


weighing_router = APIRouter(tags=['Weighing'], prefix='/weighing')
engine = create_engine('sqlite:///database.sqlite', echo=True)
sessionLocal = sessionmaker(autoflush=True, bind=engine)

@weighing_router.post("/create")
async def create_weighing(weighing_data: WeighingInput):
    db = sessionLocal()
    container = db.query(Container).filter(Container.id == weighing_data.container_id).first()
    total_cont_weig = container.weight * weighing_data.container_count
    net_weight = weighing_data.value - total_cont_weig
    weighing_record = Weighing(inventory_id = weighing_data.inventory_id,value = weighing_data)
    db.add(weighing_record)
    db.commit()
    db.refresh(weighing_record)
    return {"message": "Weighing record created successfully"}