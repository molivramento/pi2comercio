import ormar
import shutil
from uuid import uuid4
from pydantic import BaseModel
from fastapi import HTTPException, status


"""
Não Altere o código abaixo!
Crie um arquivo em app/services/ e herde BaseServices
def __init__(self):
    super().__init__(model=Exemplo, path='exemplos'...)
"""


class BaseService:
    def __init__(self, model, path: str = None, unique_field=None, related: list[str] = None):
        """
        :param model: schema model
        :param unique_field: schema *UniqueField
        :param related: list of related models
        """
        self.model = model
        self.related = related
        self.unique_field = unique_field
        self.path = path

    async def upload(self, file):
        # TODO: 5000000 = 5MB (MAX SIZE), NEED SETTING IN ENV OR CONFIG
        # TODO: NEED ADD MINE TYPE VALIDATION (JPEG, PNG, SVG, WEBP), NEED SETTING IN ENV OR CONFIG
        # TODO: NEED VERIFY FILE EXISTS
        if file and file.size < 5000000:
            directory = f'static/{self.path}/{file.filename}'
            with open(f"{directory}", "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        else:
            directory = f'static/{self.path}/default.pdf'
        return directory

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

    async def create(self, payload: BaseModel):
        await self.verify_unique_field(payload)
        return await self.model.objects.create(**payload.dict(), id=uuid4())

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

    async def update(self, payload):
        # TODO: verificar se os novos dados possuem campos unicos conflitantes
        # buscar o payload no banco de dados, verificar se os campos unicos registrados no banco de dado
        # possuem o mesmo ID que o payload que será alterado
        # await self.verify_unique_field(payload)
        try:
            obj = await self.model.objects.get(id=payload.id)
            return await obj.update(**payload.dict())
        except ormar.exceptions.NoMatch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'{self.model.__name__} not found')

    async def delete(self, pk: uuid4):
        try:
            obj = await self.model.objects.get(id=pk)
            return await obj.delete()
        except ormar.exceptions.NoMatch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{self.model.__name__} not found')
