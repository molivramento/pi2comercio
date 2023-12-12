from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
from app.models.places import Place
from app.schemas.places import PlaceIn, PlaceFilter

from app.services.places import places_service
from typing import List

router = APIRouter()


@router.get("/")
async def get_places(filters: PlaceFilter = Depends()):
    return await places_service.get(filters)


@router.post("/")
async def create_places(data: PlaceIn):
    return await places_service.create(payload=data)


@router.put("/", response_model=Place | dict)
async def update_places(payload: Place):
    return await places_service.update(payload=payload)


@router.delete("/{uuid}")
async def delete_places(uuid: UUID):
    return await places_service.delete(uuid=uuid)