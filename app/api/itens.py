from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
<<<<<<< HEAD
from app.models.itens import Itens
from app.schemas.itens import itensIN, itensFilter

from app.services.itens import Itens_service

router = APIRouter()

@router.get("/", response_model=list[Itens] | dict)
async def get_itens(filters: itensFilter = Depends()):
    return await Itens_service.get(filters)


@router.post("/")
async def create_iten(data: itensIN):
    return await Itens_service.create(payload=data)


@router.put("/", response_model=Itens | dict)
async def update_iten(payload: Itens):
    return await Itens_service.update(payload=payload)
=======
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
>>>>>>> fbe94ee0bf0dd76cbbd81f5559c511db5e196914


@router.delete("/{uuid}")
async def delete_iten(uuid: UUID):
<<<<<<< HEAD
    return await Itens_service.delete(uuid=uuid)
=======
    return await items_service.delete(uuid=uuid)
>>>>>>> fbe94ee0bf0dd76cbbd81f5559c511db5e196914
