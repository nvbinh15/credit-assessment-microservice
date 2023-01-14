from typing import Optional 
from pydantic import BaseModel


class LoanBase(BaseModel):
    amount: int 


class Loan(LoanBase):
    id: int

    class Config:
        orm_mode = True