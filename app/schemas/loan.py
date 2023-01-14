from typing import Optional 
from pydantic import BaseModel
from enum import IntEnum 


class LoanStatus(IntEnum):
    pending = 0
    accepted = 1
    rejected = -1 


class LoanPrediction(IntEnum):
    accepted = 1
    rejected = -1 
        

class LoanBase(BaseModel):
    amount: int 
    term: int # by month
    prediction: bool 
    status: LoanStatus = LoanStatus.pending


class Loan(LoanBase):
    id: int

    class Config:
        orm_mode = True