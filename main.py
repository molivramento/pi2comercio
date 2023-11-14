import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database import config_database

from app.api.products import router as product_router

config_database()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(product_router, prefix='/products', tags=['Product'])

origins = ['http://localhost:9000',
           'http://127.0.0.1:9000']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

# TODO: TEST AWS BUCKET (BOTO3)
load_dotenv()


aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket_name = os.getenv('BUCKET_NAME')

