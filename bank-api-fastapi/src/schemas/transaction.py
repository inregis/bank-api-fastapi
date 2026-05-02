from pydantic import BaseModel

class TransactionIn(BaseModel):
    amount: float
    type: str

class TransactionOut(BaseModel):
    id: int
    amount: float
    type: str

    class Config:
        from_attributes = True