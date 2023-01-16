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
    new_loan = models.Loan(
        description=request.description, amount=request.amount, term=request.term, 
        coapplicant_income=request.coapplicant_income, status=request.status, user_id=current_user.id
    )
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan


@router.get('/{id}')
def get_loan(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    loan = db.query(models.Loan) \
        .filter(models.Loan.user_id == current_user.id) \
        .filter(models.Loan.id == id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan


@router.put('/{id}', status_code=201, response_model=Loan)
def update_loan(id: int, request: LoanBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    loan_db = db.query(models.Loan).filter(models.Loan.user_id == current_user.id).filter(models.Loan.id == id)
    if not loan_db.first():
        raise HTTPException(status_code=404, detail='Loan not found')
    loan_db.update(request.dict(exclude_unset=True))
    db.commit()
    db.refresh(loan_db.first())
    return loan_db.first()


@router.delete('/{id}')
def delete_loan(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    loan_db = db.query(models.Loan).filter(models.Loan.user_id == current_user.id).filter(models.Loan.id == id)
    if not loan_db.first():
        raise HTTPException(status_code=404, detail='Loan not found')
    loan_db.delete(synchronize_session=False)
    db.commit()
    return {'details': 'deleted'}
