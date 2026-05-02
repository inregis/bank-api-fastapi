from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.schemas.user import UserCreate, UserLogin
from src.services.user import UserService
from src.security import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Auth"])


@router.post("/register")
async def register(data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await UserService().create(db, data)


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db=Depends(get_db)
):
    return await UserService().login(
        db,
        form_data.username,
        form_data.password
    )
