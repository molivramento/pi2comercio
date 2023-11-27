from app.services.base import BaseService
from app.models.products import Products


class ProductService(BaseService):
    def __init__(self):
        super().__init__(model=Products,
                         path='products',
                         related=None)


product_service = ProductService()
