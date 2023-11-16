from app.services.base import BaseService
from app.models.transation import Transation


class TransationService(BaseService):
    def __init__(self):
        super().__init__(model=Transation,
                         path='transation',
                         related=None)


Transation_service = TransationService()
