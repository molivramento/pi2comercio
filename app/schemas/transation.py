from typing import Optional
from pydantic import BaseModel

from app.models.transation import Transation
from app.schemas.base import BaseFilter

transationIN = Transation.get_pydantic(
    exclude={
        "uuid",
    }
)


class TransationFilter(BaseFilter):
    total_amount: Optional[float] = None
    date: Optional[date] = None
