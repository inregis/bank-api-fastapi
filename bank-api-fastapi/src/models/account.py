from sqlalchemy import Column, Integer, Float
from src.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float, default=0)