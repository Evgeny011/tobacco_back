from fastapi import FastAPI

from queries.inventory_router import inventory_router

import sqlalchemy_tabak


app = FastAPI(
    title= 'Inventory calculator'
)
app.include_router(inventory_router)