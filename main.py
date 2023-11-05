import os

import boto3
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from database import config_database

from app.api.products import router as product_router

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

# TODO: TEST AWS BUCKET (BOTO3)
load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket_name = os.getenv('BUCKET_NAME')

s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)


@app.post('/')
async def upload_file(file: UploadFile = None):
    s3.upload_fileobj(file.file, bucket_name, file.filename)
    return file.filename
