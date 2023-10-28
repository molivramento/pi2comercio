from fastapi import FastAPI
from database import config_database

from app.products.api import router as product_router

config_database()

app = FastAPI()

app.include_router(product_router, prefix='/products', tags=['Product'])
