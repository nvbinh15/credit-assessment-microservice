from pydantic import BaseModel
from .loan import LoanStatus, LoanPrediction
from .user import Gender, CreditType, PropertyArea
from enum import Enum


class LoanPredictionRequest(BaseModel):
    gender: Gender = Gender.male
    is_married: bool = False
    dependents: int = 0
    graduated: bool = True 
    is_self_employed: bool = False 
    applicant_monthly_income: float = 0
    coapplicant_income: float = 0
    loan_amount: float = 0
    loan_amount_term_in_days: int = 360
    credit_history: CreditType = CreditType.good
    property_area: PropertyArea = PropertyArea.urban

    class Config:
        orm_mode = True 


class CreditMix(str, Enum):
    not_available = "Not available"
    standard = "Standard"
    good = "Good"
    bad = "Bad"


class PayMentMinAmtType(str, Enum):
    yes = 'Yes'
    no = 'No'
    nm = 'NM'


class CreditClassificationRequest(BaseModel):
    age: int = 0
    annual_income: float = 0 
    number_of_bank_accounts: int = 1
    number_of_credit_cards: int = 1
    number_of_loans: int = 1
    number_of_day_delay_from_due_date: int = 0
    number_of_delay_payments: int = 0
    changed_credit_limit: float = 0
    number_of_credit_inquiries: int = 0
    credit_mix: CreditMix = CreditMix.not_available
    outstanding_debt: float = 0
    payment_of_min_amount: PayMentMinAmtType = PayMentMinAmtType.yes
    total_EMI_per_month: float = 0
    amount_invested_monthly: float = 0

    class Config:
        orm_mode = True 
