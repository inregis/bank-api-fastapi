from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.services.transaction import TransactionService
from src.security import get_current_user

router = APIRouter(tags=["Transactions"])

@router.post("/{account_id}/deposit")
async def deposit(
    account_id: int,
    amount: float,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    return await TransactionService().deposit(db, account_id, amount)


@router.post("/{account_id}/withdraw")
async def withdraw(
    account_id: int,
    amount: float,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    return await TransactionService().withdraw(db, account_id, amount)

@router.get("/{account_id}/statement")
async def statement(
    account_id: int,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    return await TransactionService().statement(db, account_id)