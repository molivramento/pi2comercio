import ormar
import shutil
from uuid import uuid4
from pydantic import BaseModel
from fastapi import HTTPException, status


class BaseService:
    def __init__(self, model, unique_field=None, related: list[str] = None):
        """
        :param model: schema model
        :param unique_field: schema *UniqueField
        :param related: list of related models
        """
        self.model = model
        self.related = related
        self.unique_field = unique_field

    async def verify_unique_field(self, payload: BaseModel = None):
        payload = self.unique_field(**payload.dict())
        if self.unique_field and payload is not None:
            query = self.model.objects
            filters_params = {k: v for k, v in payload.dict().items() if v}
            try:
                response = await query.filter(**filters_params).first()
                if response is not None:
                    raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                        detail=f'{self.model.__name__} already exists')
            except ormar.exceptions.NoMatch:
                pass

    async def get(self, filters: BaseModel):
        query = self.model.objects
        filters_params = {k: v for k, v in filters.dict().items() if v}
        if self.related:
            response = query.prefetch_related(self.related).filter(**filters_params)
        else:
            response = query.filter(**filters_params)
        if response is None:
            response = []
        else:
            response = await response.all()
        return response

    async def create(self, payload: BaseModel, file):
        # TODO: 5000000 = 5MB (MAX SIZE), NEED SETTING IN ENV OR CONFIG
        # TODO: NEED ADD MINE TYPE VALIDATION (JPEG, PNG, SVG, WEBP), NEED SETTING IN ENV OR CONFIG
        # TODO: NEED VERIFY FILE EXISTS
        if file and file.size < 5000000:
            directory = f'static/products/{file.filename}'
            with open(f"{directory}", "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        else:
            directory = f'static/products/default.pdf'
        await self.verify_unique_field(payload)
        return await self.model.objects.create(**payload.dict(), img=directory, id=uuid4())

    async def update(self, payload, file):
        # TODO: Need a function to delete the old file
        obj = await self.model.objects.get(id=payload.id)
        if file and file.size < 5000000:
            old_file = obj.img
            payload.img = f'static/products/{file.filename}'
            with open(f"{payload.img}", "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            if old_file != payload.img:
                try:
                    shutil.rmtree(old_file)
                except FileNotFoundError:
                    pass
        elif obj.img is None:
            payload.img = 'static/products/default.png'
        return await obj.update(**payload.dict())

    async def delete(self, pk: uuid4):
        obj = await self.model.objects.filter(id=pk).first()
        if obj is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{self.model.__name__} not found')
        return await obj.delete()
