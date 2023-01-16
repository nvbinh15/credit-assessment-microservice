from fastapi import APIRouter, Query
from app.schemas.credit import LoanPredictionRequest, CreditClassificationRequest
from app.ml.inference import loan_inference, credit_inference


router = APIRouter(prefix='/credit', tags=['Credit'])

@router.put('/sme')
def get_sme_loan(
    acc_recv: int = Query(0, description='Account receivable'), 
    inventories: int = Query(0, description='Inventory value'), 
    properties: int = Query(0, description='Properties and equipments value')
):
    """Calculate expected loan amount for SME by using collateral analysis """
    collateral = inventories + properties
    expected_loan = 0.8 * acc_recv + 0.5 * collateral
    return {'expected_loan': expected_loan}


@router.put('/individual/credit')
def get_credit_bucket(request: CreditClassificationRequest):
    """Classify individual's credit score into one of 3 groups: Good, Standard, or Poor"""
    credit_pred = credit_inference(request)
    if credit_pred[0] == 0:
        prediction = 'Good'
    elif credit_pred[0] == 1:
        prediction = 'Poor'
    else:
        prediction = 'Standard'
    return {'credit_type': prediction}


@router.put('/individual/loan')
def get_loan_prediction(request: LoanPredictionRequest):
    """Predict whether a personal loan will be accepted"""
    loan_pred = loan_inference(request)
    if loan_pred[0] == 'N':
        prediction = 'rejected'
    else:
        prediction = 'accepted'
    return {'loan_prediction': prediction}

