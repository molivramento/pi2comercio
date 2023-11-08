from app.schemas.products import ProductUniqueField
from app.services.base import BaseService
from app.models.products import Product


class ProductService(BaseService):
    def __init__(self):
        super().__init__(model=Product, related=None, unique_field=ProductUniqueField)

    async def create(self, payload: Product, file):
        return await super().create(payload, file)

