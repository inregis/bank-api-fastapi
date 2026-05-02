from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.controllers import transaction
from src.database import engine, Base, SessionLocal
from src.models.account import Account
from sqlalchemy import select
from src.exceptions import BusinessException
from src.controllers import auth, account
from src.models.transaction import Transaction

app = FastAPI()

app.include_router(transaction.router, prefix="/transactions")
app.include_router(account.router, prefix="/accounts")
app.include_router(auth.router, prefix="/auth")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def create_test_account():
    async with SessionLocal() as session:
        account = Account(balance=1000)
        session.add(account)
        await session.commit()

@app.on_event("startup")
async def create_test_account():
    async with SessionLocal() as session:
        result = await session.execute(select(Account))
        account = result.scalars().first()

        if not account:
            account = Account(balance=1000)
            session.add(account)
            await session.commit()

@app.exception_handler(BusinessException)
async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=400,
        content={"error": exc.message},
)



