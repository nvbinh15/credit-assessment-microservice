from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String) 
    hashed_password = Column(String)

    full_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    is_married = Column(Boolean)
    dependents = Column(Integer)
    graduated = Column(Boolean)
    is_self_employed = Column(Boolean)
    monthly_income = Column(Integer)
    property_area = Column(String)
    credit_type = Column(String)

    loans = relationship('Loan', back_populates='owner')
    

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    amount = Column(Integer)
    term = Column(Integer)
    coapplicant_income = Column(Integer)
    prediction = Column(Boolean)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='loans')
