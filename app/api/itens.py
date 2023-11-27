from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
from app.models.itens import iten
from app.schemas.itens import itenIn, itenFilter

from app.services.itens import iten_service

router = APIRouter()


@router.get("/", response_model=list[iten] | dict)
async def get_itens(filters: itenFilter = Depends()):
    return await iten_service.get(filters)


@router.post("/")
async def create_iten(data: itenIn):
    return await iten_service.create(payload=data)


@router.put("/", response_model=iten | dict)
async def update_iten(payload: iten):
    return await iten_service.update(payload=payload)


@router.delete("/{uuid}")
async def delete_iten(uuid: UUID):
    return await iten_service.delete(uuid=uuid)
