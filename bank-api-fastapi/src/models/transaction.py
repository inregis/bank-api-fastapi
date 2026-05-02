from sqlalchemy import Column, Integer, Float, String, ForeignKey
from src.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    type = Column(String)
    amount = Column(Float)