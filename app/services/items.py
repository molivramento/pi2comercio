from app.services.base import BaseService
from app.models.items import items
from app.models.products import Products
from app.models.transaction import Transaction

from fastapi import HTTPException, status
from uuid import UUID

class ItemsService(BaseService):
    def __init__(self):
        super().__init__(model=items, path='items', related=None)


items_service = ItemsService()
