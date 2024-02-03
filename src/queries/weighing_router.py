from fastapi import APIRouter

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from pydantic import BaseModel


weighing_router = APIRouter(tags=['weighing'], prefix='/weighing')
engine = create_engine('sqlite:///database.sqlite', echo=True)
sessionLocal = sessionmaker(autoflush=True, bind=engine)

