from uuid import UUID

from fastapi import APIRouter, Depends

from app.schemas.users import UserFilter, UserOut, UserIn, CreateUserIn
from app.services.users import user_service

router = APIRouter()


@router.get("/", response_model=list[UserOut] | dict)
async def get_users(filters: UserFilter = Depends()):
    return await user_service.get(filters)


@router.post("/", response_model=UserOut | dict)
async def create_user(data: CreateUserIn): # type: ignore
    return await user_service.create(payload=data)


@router.put("/", response_model=UserOut | dict)
async def update_user(payload: UserOut): # type: ignore
    return await user_service.update(payload=payload)


@router.delete("/{uuid}")
async def delete_user(uuid: UUID):
    return await user_service.delete(uuid=uuid)
