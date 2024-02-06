from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
from app.models.items import items
from app.schemas.items import itenIn, itenFilter

from app.services.items import items_service
from typing import List

router = APIRouter()

@router.get("/")
async def get_products(transaction: UUID):
    return await items.objects.filter(transation__uuid=transaction).all()


@router.post("/")
async def create_iten(data: itenIn):
    return await items_service.create(payload=data)


@router.put("/", response_model=items | dict)
async def update_iten(payload: items):
    return await items_service.update(payload=payload)


@router.delete("/{uuid}")
async def delete_iten(uuid: UUID):
    return await items_service.delete(uuid=uuid)
