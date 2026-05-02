from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.account import Account


class AccountService:

    async def get(self, db: AsyncSession, account_id: int):
        result = await db.execute(
            select(Account).where(Account.id == account_id)
        )
        account = result.scalars().first()
        return account