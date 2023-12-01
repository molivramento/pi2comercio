from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.models.bills import Bill

BillIn = Bill.get_pydantic(
    exclude={
        'uuid',
        'is_paid',
        'payment_date'
    }
)


class BillFilter(BaseModel):
    uuid: Optional[UUID] = None
    name: Optional[str] = None
    name__icontains: Optional[str] = None
    business: Optional[str] = None
    business__icontains: Optional[str] = None
    febraban: Optional[str] = None
    amount__gte: Optional[float] = None
    amount__lte: Optional[float] = None
    due_date__gte: Optional[date] = None
    due_date__lte: Optional[date] = None
    payment_date__gte: Optional[str] = None
    payment_date__lte: Optional[str] = None
    is_paid: Optional[bool] = None
