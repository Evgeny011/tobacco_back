from fastapi import FastAPI

from queries.router_create import Create_Inventory_rout

import sqlalchemy_tabak


app = FastAPI(
    title= 'Inventory calculator'
)
app.include_router(Create_Inventory_rout)