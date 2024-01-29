from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
from app.models.transaction import Transaction
from app.schemas.transaction import transactionIN, TransactionFilter

from app.services.transaction import Transaction_service

router = APIRouter()

@router.get("/", response_model=list[Transaction] | dict)
async def get_transactions(filters: TransactionFilter = Depends()):
    return await Transaction_service.get(filters)


@router.post("/")
async def create_transaction(data: transactionIN):
    return await Transaction_service.create(payload=data)


@router.put("/", response_model=Transaction | dict)
async def update_transaction(payload: Transaction):
    return await Transaction_service.update(payload=payload)


@router.delete("/{uuid}")
async def delete_transaction(uuid: UUID):
    return await Transaction_service.delete(uuid=uuid)
