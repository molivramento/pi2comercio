from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.services.security import create_token, get_current_user
from app.schemas.users import UserFilter, UserOut, UserIn
from app.services.users import user_service
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/token")
async def get_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await user_service.get(UserFilter(email=form_data.username))
    try:
        return await create_token(data={'sub': str(user[0].uuid),
                                        'email': user[0].email,
                                        'is_staff': user[0].is_staff,
                                        'is_superuser': user[0].is_superuser})
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with email {form_data.username} not found")


@router.get("/me", response_model=UserOut)
async def get_me(current_user: Annotated[UserOut, Depends(get_current_user)]):
    return current_user[0]


@router.post("/register", response_model=UserOut)
async def register(payload: UserIn):
    return await user_service.create(payload=payload)
