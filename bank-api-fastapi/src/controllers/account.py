from fastapi import Depends, APIRouter
from src.security import get_current_user
from src.database import get_db
from src.services.account import AccountService


router = APIRouter(tags=["Accounts"])



@router.get("/accounts")
async def listar_contas(user=Depends(get_current_user)):
    return {"user": user}

@router.get("/")
async def listar(user=Depends(get_current_user)):
    return []

