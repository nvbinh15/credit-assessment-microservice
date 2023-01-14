from fastapi import APIRouter, Depends, HTTPException
from typing import List 
from sqlalchemy.orm import Session 

from app.database import get_db
from app.schemas.loan import Loan, LoanBase
from app.schemas.user import User
from app.utils.oauth2 import get_current_user

from .. import database, models

router = APIRouter(
    prefix='/loan',
    tags=['Loan']
)


@router.get('', response_model=List[Loan])
def get_all_loans(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    loans = db.query(models.Loan).filter(models.Loan.user_id == current_user.id).all()
    return loans 


@router.post('', status_code=201, response_model=Loan)
def create_loan(request: LoanBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_loan = models.Loan(amount=request.amount, user_id=current_user.id)
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan
