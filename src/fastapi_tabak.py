from fastapi import FastAPI

from src.queries.inventory_router import inventory_router

import src.sqlalchemy_tabak


app = FastAPI(
    title= 'Inventory calculator'
)
app.include_router(inventory_router)
