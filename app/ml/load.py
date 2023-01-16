from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import ExtraTreesClassifier, HistGradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

from app.schemas.credit import LoanPredictionRequest, CreditClassificationRequest
from app.schemas.user import CreditType, Gender, PropertyArea
import numpy as np


def get_loan_model_scaler():
    loan_scaler = MinMaxScaler()

    df = pd.read_csv('data/loan-prediction.csv')
    df.drop(columns=['Loan_ID'], inplace=True)
    for column in df.columns:
        if df[column].dtypes == 'object' or column in ['Credit_History', 'Loan_Amount_Term']:
            if df[column].isnull().sum() > 0:
                df[column].fillna(df[column].mode()[0], inplace=True)

    for column in df.columns:
        if df[column].dtypes != 'object':
            if df[column].isnull().sum() > 0:
                df[column].fillna(df[column].mean(), inplace=True)

    X = df.drop(['Loan_Status'], axis=1)
    y = df['Loan_Status']
    X = pd.get_dummies(X)
    X = loan_scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    loan_model = DecisionTreeClassifier(max_leaf_nodes=100)
    loan_model.fit(X_train, y_train)
    return loan_model, loan_scaler


train_df = pd.read_csv(f'data/credit-score/train.csv', low_memory=False)
train_df.drop(
    columns=[
        'ID', 'Customer_ID', 'Month', 'SSN', 'Name', 'Occupation', 'Credit_Utilization_Ratio', 'Payment_Behaviour',
        'Monthly_Inhand_Salary', 'Type_of_Loan', 'Credit_History_Age', 'Monthly_Balance', 'Interest_Rate'
    ], 
    inplace=True
)
for index, row in train_df.iterrows():
    if isinstance(row['Age'], str):
        if row['Age'][-1] == '_':
            train_df.loc[index, 'Age'] = int(row['Age'][:-1])

train_df['Age'] = pd.to_numeric(train_df['Age'])
train_df = train_df[(train_df['Age'] > 0) & (train_df['Age'] < 150)]

for index, row in train_df.iterrows():
    if isinstance(row['Num_of_Delayed_Payment'], str):
        if row['Num_of_Delayed_Payment'][-1] == '_':
            train_df.loc[index, 'Num_of_Delayed_Payment'] = int(row['Num_of_Delayed_Payment'][:-1])

train_df['Num_of_Delayed_Payment'].fillna(0, inplace=True)
train_df['Num_Credit_Inquiries'].fillna(0, inplace=True)
train_df['Amount_invested_monthly'].fillna(0, inplace=True)
train_df['Changed_Credit_Limit'].fillna(0, inplace=True)

train_df = train_df.applymap(lambda x: x if x is np.NaN or not isinstance(x, str) else str(x).strip('_ ,"'))
train_df['Num_of_Delayed_Payment'] = pd.to_numeric(train_df['Num_of_Delayed_Payment'])
train_df['Amount_invested_monthly'] = pd.to_numeric(train_df['Amount_invested_monthly'])
train_df['Annual_Income'] = pd.to_numeric(train_df['Annual_Income'])
train_df['Num_of_Loan'] = pd.to_numeric(train_df['Num_of_Loan'])
train_df['Outstanding_Debt'] = pd.to_numeric(train_df['Outstanding_Debt'])
train_df['Changed_Credit_Limit'] = pd.to_numeric(train_df['Changed_Credit_Limit'])
train_df['Changed_Credit_Limit'].fillna(0, inplace=True)

ordinal_encoder = OrdinalEncoder()

for column in train_df.columns:
    if train_df[column].dtypes == 'object':
        train_df[column] = ordinal_encoder.fit_transform(train_df[column].values.reshape(-1,1))

X = train_df.drop('Credit_Score', axis=1)
y = train_df['Credit_Score']
mms = MinMaxScaler()
X = mms.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

hgb = HistGradientBoostingClassifier()
hgb.fit(X_train, y_train)

def get_credit_model_scaler():
    return hgb, mms


