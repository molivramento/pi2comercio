from app.models.bills import Bill
from app.services.base import BaseService


class BillService(BaseService):
    def __init__(self):
        super().__init__(model=Bill,
                         path='bills',
                         related=None)


bill_service = BillService()
