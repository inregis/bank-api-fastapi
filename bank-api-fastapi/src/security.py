from jose import jwt
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from src.config import settings
from jose import JWTError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = HTTPBearer()


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.access_token_expire_minutes
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm
    )

async def get_current_user(token=Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token.credentials,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )

        username = payload.get("sub")

        if not username:
            raise HTTPException(status_code=401, detail="Token inválido")

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="Token expirado")