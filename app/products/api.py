from uuid import uuid4, UUID

import ormar
from fastapi import APIRouter, HTTPException

from app.products.models import Product
from app.products.schemas import ProductIn

router = APIRouter()


@router.get("/", response_model=list[Product] | dict)
async def get_products():
    return await Product.objects.all()


@router.post("/", response_model=Product | dict)
async def create_product(payload: ProductIn):
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
