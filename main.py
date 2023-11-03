import boto3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import config_database

from app.products.api import router as product_router

config_database()

app = FastAPI()

app.include_router(product_router, prefix='/products', tags=['Product'])

origins = ['http://localhost:9000',
           'http://127.0.0.1:9000']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

