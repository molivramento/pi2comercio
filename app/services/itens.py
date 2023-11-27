from app.services.base import BaseService
from app.models.itens import Itens


class ItensService(BaseService):
    def __init__(self):
        super().__init__(model=Itens,
                         path='itens',
                         related=None)


Itens_service = ItensService()