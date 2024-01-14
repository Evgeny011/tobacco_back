from fastapi import FastAPI

from queries.router import Create_Inventory_rout


app = FastAPI(
    title= 'Inventory calculator'
)
app.include_router(Create_Inventory_rout)

