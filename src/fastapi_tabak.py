from fastapi import FastAPI

from src.queries.inventory_router import inventory_router

import src.sqlalchemy_tabak

from fastapi.middleware.cors import CORSMiddleware


ALLOW_ORIGINS = ["*"]

app = FastAPI(
    title= 'Inventory calculator'
)
app.include_router(inventory_router)

app.add_middleware(
    CORSMiddleware, allow_origins=ALLOW_ORIGINS, allow_credentials=True
)