import os
from datetime import datetime, timedelta
from typing import Annotated

from dotenv import load_dotenv
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext

from app.schemas.users import UserFilter, UserIn
from app.services.users import user_service

load_dotenv()

SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')


async def hash_password(password: str):
    return pwd_context.hash(password)


async def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


async def authenticate_user(payload: UserIn):
    user = await user_service.search(UserFilter(email=payload.email))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with email {payload.email} not found")
    if not await verify_password(payload.password, user[0].password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect password")
    if not user[0].is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Inactive user")
    return user[0]


async def create_token(data: dict) -> dict:
    enc = data.copy()
    access_expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    enc.update({'exp': access_expire})
    access_token = jwt.encode(enc, SECRET_ACCESS_KEY, ALGORITHM)
    return {'access_token': access_token}


async def decode_token(access_token: str):
    try:
        return jwt.decode(access_token, SECRET_ACCESS_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Access token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid token")


async def get_current_user(access_token: Annotated[str, Depends(oauth2_scheme)]):
    payload = await decode_token(access_token=access_token)
    return await user_service.get(UserFilter(email=payload['email']))
