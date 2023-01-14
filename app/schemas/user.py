from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True