from typing import Optional

from app.models.transaction import Transaction
from app.schemas.base import BaseFilter

transactionIN = Transaction.get_pydantic(
    exclude={
        "uuid",
    }
)


class TransactionFilter(BaseFilter):
    date: Optional[date] = None
