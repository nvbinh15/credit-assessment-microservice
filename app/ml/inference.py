from .load import get_loan_model_scaler, get_credit_model_scaler
import pandas as pd
from app.schemas.credit import LoanPredictionRequest, CreditClassificationRequest, CreditMix, PayMentMinAmtType
from app.schemas.user import CreditType, Gender, PropertyArea
import numpy as np


def loan_inference(data: LoanPredictionRequest):
    transformed = [
        data.applicant_monthly_income, data.coapplicant_income, data.loan_amount, 
        data.loan_amount_term_in_days
    ]

    if data.credit_history == CreditType.poor:
        transformed.append(0.0)
    else:
        transformed.append(1.0)

    if data.gender == Gender.male:
        transformed.extend([0, 1])
    else: 
        transformed.extend([1, 0])

    if data.is_married:
        transformed.extend([0, 1])
    else:
        transformed.extend([1, 0])

    if data.dependents == 0:
        transformed.extend([1, 0, 0, 0])
    elif data.dependents == 1:
        transformed.extend([0, 1, 0, 0])
    elif data.dependents == 2:
        transformed.extend([0, 0, 1, 0])
    else: 
        transformed.extend([0, 0, 0, 1])

    if data.graduated:
        transformed.extend([1, 0])
    else:
        transformed.extend([0, 1])

    if data.is_self_employed:
        transformed.extend([0, 1])
    else:
        transformed.extend([1, 0])

    if data.property_area == PropertyArea.rural:
        transformed.extend([1, 0, 0])
    elif data.property_area == PropertyArea.semiurban:
        transformed.extend([0, 1, 0])
    else: 
        transformed.extend([0, 0, 1])

    loan_model, loan_scaler = get_loan_model_scaler()
    transformed = loan_scaler.transform(np.array(transformed).reshape(1, -1))
    return loan_model.predict(transformed)


def credit_inference(data: CreditClassificationRequest):
    credit_model, credit_scaler = get_credit_model_scaler()
    transformed = [
        data.age, data.annual_income, data.number_of_bank_accounts,
        data.number_of_credit_cards, data.number_of_loans, data.number_of_day_delay_from_due_date,
        data.number_of_delay_payments, data.changed_credit_limit, 
        data.number_of_credit_inquiries
    ]

    if data.credit_mix == CreditMix.not_available:
        transformed.append(0)
    elif data.credit_mix == CreditMix.bad:
        transformed.append(1)
    elif data.credit_mix == CreditMix.good:
        transformed.append(2)
    else:
        transformed.append(3)

    transformed.append(data.outstanding_debt)

    if data.payment_of_min_amount == PayMentMinAmtType.nm:
        transformed.append(0)
    elif data.payment_of_min_amount == PayMentMinAmtType.no:
        transformed.append(1)
    else:
        transformed.append(2)

    transformed.extend([
        data.total_EMI_per_month, data.amount_invested_monthly
    ])

    transformed = credit_scaler.transform(np.array(transformed).reshape(1,-1))
    return credit_model.predict(transformed)
