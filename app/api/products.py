import ormar
from uuid import uuid4, UUID
from fastapi import APIRouter, HTTPException, UploadFile, Depends, File
from app.models.products import Product
from app.schemas.products import ProductIn, GetProduct

from app.services.products import ProductService

router = APIRouter()

product_service = ProductService()


@router.get("/", response_model=list[Product] | dict)
async def get_products(filters: GetProduct = Depends()):
    return await product_service.get(filters)


@router.post("/")
async def create_product(data: ProductIn, file: UploadFile | None = None):
    return await product_service.create(payload=data, file=file)


@router.put("/", response_model=Product | dict)
async def update_product(payload: ProductIn, file: UploadFile | None = None):
    return await product_service.update(payload=payload, file=file)
    # try:
    #     product = await Product.objects.get(id=payload.id)
    #     return await product.update(**payload.dict())
    # except ormar.exceptions.NoMatch:
    #     raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/{pk}")
async def delete_product(pk: UUID):
    try:
        product = await Product.objects.get(id=pk)
        return await product.delete()
    except ormar.exceptions.NoMatch:
        raise HTTPException(status_code=404, detail="Product not found")
