from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
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


@router.delete("/{uuid}")
async def delete_iten(uuid: UUID):
    return await Itens_service.delete(uuid=uuid)
