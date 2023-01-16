from typing import Optional
from pydantic import BaseModel, EmailStr
from enum import Enum, IntEnum


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class CreditType(str, Enum):
    poor = 'poor'
    standard = 'standard'
    good = 'good'


class PropertyArea(str, Enum):
    rural = 'rural'
    semiurban = 'semiurban'
    urban = 'urban'


class Profile(BaseModel):
    full_name: Optional[str]
    age: Optional[int]
    gender: Optional[Gender] = Gender.male
    is_married: Optional[bool] = True  
    dependents: Optional[int] = 0
    graduated: Optional[bool]
    is_self_employed: Optional[bool] = False 
    monthly_income: Optional[int] 
    property_area: Optional[PropertyArea]
    credit_bucket: Optional[CreditType]

    class Config:
        orm_mode = True 


class UserProfile(User, Profile):
    
    class Config:
        orm_mode = True