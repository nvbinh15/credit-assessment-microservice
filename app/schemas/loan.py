from typing import Optional 
from pydantic import BaseModel
from enum import Enum 
from fastapi import Query


class LoanStatus(str, Enum):
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'


class LoanPrediction(str, Enum):
    accepted = 'accepted'
    rejected = 'rejected'
        

class LoanBase(BaseModel):
    description: Optional[str]
    amount: Optional[int] 
    term: Optional[int] = Query(None, description="Loan term by day")
    coapplicant_income: Optional[int] = 0
    status: Optional[LoanStatus] = LoanStatus.pending

    class Config:
        orm_mode = True 


class Loan(LoanBase):
    id: int
    user_id: int 

    class Config:
        orm_mode = True


class LoanWithPred(BaseModel):
    prediction: bool 

    class Config:
        orm_mode = True
