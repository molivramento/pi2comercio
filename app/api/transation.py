from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
from app.models.transation import Transation
from app.schemas.transation import transationIN, TransationFilter

from app.services.transation import Transation_service

router = APIRouter()

@router.get("/", response_model=list[Transation] | dict)
async def get_transations(filters: TransationFilter = Depends()):
    return await Transation_service.get(filters)


@router.post("/")
async def create_transation(data: transationIN):
    return await Transation_service.create(payload=data)


@router.put("/", response_model=Transation | dict)
async def update_transation(payload: Transation):
    return await Transation_service.update(payload=payload)


@router.delete("/{uuid}")
async def delete_transation(uuid: UUID):
    return await Transation_service.delete(uuid=uuid)
