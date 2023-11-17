from fastapi import APIRouter, Depends, Request

from app.services.security import create_token, get_current_user
from app.schemas.users import UserFilter, UserOut
from app.services.users import user_service
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/token")
async def get_token(data: OAuth2PasswordRequestForm = Depends()):
    user = await user_service.get(UserFilter(email=data.username))
    return await create_token(data={'sub': str(user[0].uuid),
                                    'email': user[0].email,
                                    'is_staff': user[0].is_staff,
                                    'is_superuser': user[0].is_superuser})


@router.get("/me", response_model=UserOut, dependencies=[Depends(get_current_user)])
async def get_me(request: Request):
    print(request.headers)
    return await get_current_user()
