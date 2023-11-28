from app.services.base import BaseService
from app.models.itens import itens

import sqlite3

import ormar
import shutil
from uuid import uuid4, UUID
from pydantic import BaseModel
from fastapi import HTTPException, status

class itensService(BaseService):
    def __init__(self):
        super().__init__(model=itens,
                         path='itens',
                         related=None)

    async def get(self, filters: BaseModel):
        try: 
            await itens.objects.filter()
        except:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f'{self.model.__name__} already exist')

itens_service = itensService()
