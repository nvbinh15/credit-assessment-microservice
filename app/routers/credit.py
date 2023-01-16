from fastapi import APIRouter, Query

router = APIRouter(prefix='/credit', tags=['Credit'])

@router.get('/sme', status_code=200)
def get_sme_loan(
    acc_recv: int = Query(0, description='Account receivable'), 
    inventories: int = Query(0, description='Inventory value'), 
    properties: int = Query(0, description='Properties and equipments value')
):
    """Get expected loan of SME given financial details"""
    collateral = inventories + properties
    expected_loan = 0.8 * acc_recv + 0.5 * collateral
    return {'expected_loan': expected_loan}


@router.get('/individual/bucket')
def get_credit_bucket():
    pass 


@router.get('/individual/loan')
def get_loan_prediction():
    pass 

