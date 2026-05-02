from sqlalchemy import select
from src.models.user import User
from src.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException
from src.exceptions import BusinessException

class UserService:

    async def create(self, db, data):
        user = User(
            username=data.username,
            password=hash_password(data.password)
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user

    async def authenticate(self, db, data):
        result = await db.execute(
            select(User).where(User.username == data.username)
        )

        user = result.scalar_one_or_none()

        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        return user
    
    async def login(self, db, username: str, password: str):
        result = await db.execute(select(User).where(User.username == username))
        user = result.scalars().first()

        if not user or not verify_password(password, user.password):
            raise BusinessException("Usuário ou senha inválidos")

        token = create_access_token({"sub": user.username})

        return {
            "access_token": token,
            "token_type": "bearer"
        }