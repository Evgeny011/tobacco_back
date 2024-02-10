from fastapi import APIRouter, HTTPException

from sqlalchemy import create_engine, desc

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
    if container is None:
        raise HTTPException(status_code = 404, detail = "Container not found")
    total_cont_weig = container.weight * weighing_data.container_count
    net_weight = weighing_data.value - total_cont_weig
    weighing_record = Weighing(inventory_id = weighing_data.inventory_id, value = net_weight)
    db.add(weighing_record)
    db.commit()
    db.refresh(weighing_record)
    return {"message": "Weighing record created successfully"}

@weighing_router.delete("/delete/{id}")
async def delete_weight_by_id(id: int):
    db = sessionLocal()
    weight = db.query(Weighing).filter(Weighing.id == id).first()
    if weight:
        db.delete(weight)
        db.commit()
        return {"message": "The weighing was successfully deleted"}
    else:
        return {"error": "Weighing was not deleted"}

@weighing_router.get("/get/{inventory_id}")
async def get_weighings_by_inventory_id(inventory_id: int):
    db = sessionLocal()
    weighings = db.query(Weighing).filter(Weighing.inventory_id == inventory_id).order_by(desc(Weighing.id)).all()
    if not weighings:
        raise HTTPException(status_code=404, detail="No weighings found for this inventory")
    return [{"id": w.id, "value": w.value} for w in weighings]