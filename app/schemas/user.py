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


class CreditType(IntEnum):
    poor = 0
    standard = 1
    good = 2


class Education(str, Enum):
    pass 


class PropertyArea(str, Enum):
    pass 


class UserProfile(User):
    age: Optional[int]
    gender: Gender = Gender.male
    is_married: bool = True  
    dependents: int = 0
    education: Education 
    is_self_employed: bool = False 
    income: int 
    property_area: PropertyArea
    coapplicant_income: int = 0
    credit: Optional[CreditType]

    class Config:
        orm_mode = True 
