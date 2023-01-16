from fastapi import APIRouter, Query

router = APIRouter(prefix='/credit', tags=['Credit'])

@router.get('/sme', status_code=200)
def get_sme_loan(
    acc_recv: int = Query(0, description='Account receivable'), 
    inventories: int = Query(0, description='Inventory value'), 
    properties: int = Query(0, description='Properties and equipments value')
):
    """Calculate expected loan amount for SME by using collateral analysis """
    collateral = inventories + properties
    expected_loan = 0.8 * acc_recv + 0.5 * collateral
    return {'expected_loan': expected_loan}


@router.get('/individual/bucket')
def get_credit_bucket():
    """Classify individual's credit score into one of 3 groups: Good, Standard, or Poor"""
    pass 


@router.get('/individual/loan')
def get_loan_prediction():
    """Predict whether a personal loan will be accepted"""
    pass 

