from typing import Union

from app.schemas.products import ProductUniqueField, ProductIn
from app.services.base import BaseService
from app.models.products import Product


class ProductService(BaseService):
    def __init__(self):
        super().__init__(model=Product, related=None, unique_field=ProductUniqueField)
        self.model = Product

    async def create(self, payload: ProductIn, file):
        return await super().create(payload, file)

    async def update(self, payload: ProductIn, file):
        return await super().update(payload, file)
