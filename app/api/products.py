from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
from app.models.products import Product
from app.schemas.products import ProductIn, GetProduct

from app.services.products import product_service

router = APIRouter()


@router.post("/upload")
async def upload_images(file: UploadFile):
    return await product_service.upload(file)


@router.get("/", response_model=list[Product] | dict)
async def get_products(filters: GetProduct = Depends()):
    return await product_service.get(filters)


@router.post("/")
async def create_product(data: ProductIn):
    return await product_service.create(payload=data)


@router.put("/", response_model=Product | dict)
async def update_product(payload: Product):
    return await product_service.update(payload=payload)


@router.delete("/{pk}")
async def delete_product(pk: UUID):
    return await product_service.delete(pk=pk)
