from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
from app.models.itens import itens
from app.schemas.itens import itenIn, itenFilter

from app.services.itens import itens_service
from typing import List

router = APIRouter()

@router.get("/")
async def get_products(transaction: UUID):
    return await itens.objects.filter(transation__uuid=transaction).all()


@router.post("/")
async def create_iten(data: itenIn):
    return await itens_service.create(payload=data)


@router.put("/", response_model=itens | dict)
async def update_iten(payload: itens):
    return await itens_service.update(payload=payload)


@router.delete("/{uuid}")
async def delete_iten(uuid: UUID):
    return await itens_service.delete(uuid=uuid)
