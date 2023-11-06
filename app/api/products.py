import shutil

import ormar
from uuid import uuid4, UUID
from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models.products import Product
from app.schemas.products import ProductIn

router = APIRouter()


@router.get("/", response_model=list[Product] | dict)
async def get_products():
    return await Product.objects.all()


@router.get("/{pk}", response_model=Product | dict)
async def get_product(pk: UUID):
    try:
        return await Product.objects.get(id=pk)
    except ormar.exceptions.NoMatch:
        raise HTTPException(status_code=404, detail="Product not found")


@router.get("/name/{name}", response_model=list[Product] | dict)
async def get_products_by_name(name: str):
    products = await Product.objects.filter(name__icontains=name).all()
    if products:
        return products
    raise HTTPException(status_code=404, detail="Product not found")


@router.post("/")
async def create_product(payload: ProductIn, file: UploadFile | None = None):
    if file:
        with open(f"static/products/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            payload.img = f'static/products/{file.filename}'
    else:
        payload.img = f'static/products/default.png'
    return await Product.objects.create(**payload.dict(), id=uuid4())


@router.put("/", response_model=Product | dict)
async def update_product(payload: Product):
    try:
        product = await Product.objects.get(id=payload.id)
        return await product.update(**payload.dict())
    except ormar.exceptions.NoMatch:
        raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/{pk}")
async def delete_product(pk: UUID):
    try:
        product = await Product.objects.get(id=pk)
        return await product.delete()
    except ormar.exceptions.NoMatch:
        raise HTTPException(status_code=404, detail="Product not found")
