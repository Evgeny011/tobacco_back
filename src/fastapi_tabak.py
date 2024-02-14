from fastapi import FastAPI

from src.inventory.router import inventory_router

from src.weighing.router import weighing_router

from src.container.router import container_router

import src.sqlalchemy_tabak

from fastapi.middleware.cors import CORSMiddleware


ALLOW_ORIGINS = ["*"]

app = FastAPI(
    title= 'Inventory calculator'
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://82.97.248.162:8000"  
]

app.include_router(inventory_router)
app.include_router(weighing_router)
app.include_router(container_router)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=ALLOW_ORIGINS, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)