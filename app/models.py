from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String) 
    hashed_password = Column(String)

    loans = relationship('Loan', back_populates='owner')
    

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='loans')