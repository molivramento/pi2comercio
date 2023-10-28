from uuid import uuid4, UUID

from fastapi import APIRouter

from app.products.models import Product
from app.products.schemas import ProductIn

router = APIRouter()


@router.get("/")
async def get_products():
    return await Product.objects.all()


@router.post("/")
async def create_product(payload: ProductIn):
    return await Product.objects.create(**payload.dict(), id=uuid4())


@router.put("/")
async def update_product(payload: Product):
    product = await Product.objects.get(id=payload.id)
    return await product.update(**payload.dict())


@router.delete("/{pk}")
async def delete_product(pk: UUID):
    product = await Product.objects.get(id=pk)
    return await product.delete()
