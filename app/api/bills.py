from fastapi import APIRouter, Depends

from app.models.bills import Bill
from app.schemas.bills import BillFilter, BillIn
from app.services.bills import bill_service

router = APIRouter()


@router.get('/')
async def get_bills(filters: BillFilter = Depends()):
    return await bill_service.get(filters)


@router.post('/')
async def create_bill(payload: BillIn):
    return await bill_service.create(payload)


@router.put('/')
async def update_bill(payload: Bill):
    return await bill_service.update(payload)


@router.delete('/')
async def delete_bill(payload: Bill):
    return await bill_service.delete(payload)