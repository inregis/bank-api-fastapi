from sqlalchemy import select
from src.models.account import Account
from src.models.transaction import Transaction
from src.exceptions import BusinessException


class TransactionService:

    async def deposit(self, db, account_id: int, amount: float):
        result = await db.execute(
            select(Account).where(Account.id == account_id)
        )
        account = result.scalar_one_or_none()

        if amount <= 0:
            raise BusinessException("O valor deve ser maior que zero")

        if not account:
            raise BusinessException("Conta não encontrada")

        account.balance += amount

        transaction = Transaction(
            account_id=account_id,
            type="deposit",
            amount=amount
        )

        db.add(transaction)
        await db.commit()
        await db.refresh(account)

        return {
            "message": "Depósito realizado com sucesso",
            "balance": account.balance
        }

    async def withdraw(self, db, account_id: int, amount: float):
        result = await db.execute(
            select(Account).where(Account.id == account_id)
        )
        account = result.scalar_one_or_none()

        if amount <= 0:
            raise BusinessException("O valor deve ser maior que zero")

        if not account:
            raise BusinessException("Conta não encontrada")

        if account.balance < amount:
            raise BusinessException("Saldo insuficiente")

        account.balance -= amount

        transaction = Transaction(
            account_id=account_id,
            type="withdraw",
            amount=amount
        )

        db.add(transaction)
        await db.commit()
        await db.refresh(account)

        return {
            "message": "Saque realizado com sucesso",
            "balance": account.balance
        }

    async def statement(self, db, account_id: int):
        result = await db.execute(
            select(Account).where(Account.id == account_id)
        )
        account = result.scalar_one_or_none()

        if not account:
            raise BusinessException("Conta não encontrada")

        tx_result = await db.execute(
            select(Transaction).where(Transaction.account_id == account_id)
        )

        transactions = tx_result.scalars().all()

        return {
            "account_id": account.id,
            "balance": account.balance,
            "transactions": [
                {
                    "type": t.type,
                    "amount": t.amount
                }
                for t in transactions
            ]
        }