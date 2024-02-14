from fastapi import APIRouter

from sqlalchemy import create_engine, desc

from sqlalchemy.orm import sessionmaker

from src.container.models import Container

from src.container.models import ContainerInput


container_router = APIRouter(tags=['Container'], prefix='/container')
engine = create_engine('sqlite:///database.sqlite', echo=True)
sessionLocal = sessionmaker(autoflush=True, bind=engine)

@container_router.post("/create")
async def create_container(container_input: ContainerInput):
    db = sessionLocal()
    new_container = Container(name = container_input.name, weight = container_input.weight)
    db.add(new_container)
    db.commit()
    db.refresh(new_container)
    return new_container

@container_router.delete("/delete/{id}")
async def delete_container(id: int):
    db = sessionLocal()
    delete_container = db.query(Container).filter(Container.id == id).first()
    if delete_container:
        db.delete(delete_container)
        db.commit()
        return {"message": "Container deleted successfully"}
    else:
        return {"error": "There was an error deleting the container"}

@container_router.get("/get")
async def get_conrainers():
    db = sessionLocal()
    container = db.query(Container).order_by(desc(Container.id)).all()
    return container
