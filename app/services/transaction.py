from app.services.base import BaseService
from app.models.transaction import Transaction


class TransactionService(BaseService):
    def __init__(self):
        super().__init__(model=Transaction,
                         path='transaction',
                         related=None)


Transaction_service = TransactionService()
