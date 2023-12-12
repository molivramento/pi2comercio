from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database import config_database

from app.api.products import router as product_router
from app.api.users import router as user_router
from app.api.auth import router as auth_router
from app.api.transaction import router as transaction_router
from app.api.itens import router as itens_router
<<<<<<< HEAD
from app.api.places import router as places_router
=======
from app.api.bills import router as bill_router
>>>>>>> ac63f1e24403bb2411804f8ff8a22883eb9df0b1

config_database()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(user_router, prefix='/users', tags=['Users'])
app.include_router(product_router, prefix='/products', tags=['Products'])
app.include_router(transaction_router, prefix='/transation', tags=['Transations'])
app.include_router(itens_router, prefix='/itens', tags=['Itens'])
<<<<<<< HEAD
app.include_router(places_router, prefix='/places', tags=['Places'])
=======
app.include_router(bill_router, prefix='/bills', tags=['Bills'])
>>>>>>> ac63f1e24403bb2411804f8ff8a22883eb9df0b1

origins = ['http://localhost:9000',
           'http://127.0.0.1:9000'
           'http://192.168.1.21:9000',
           'http://172.20.240.1:9000',
           '*']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
