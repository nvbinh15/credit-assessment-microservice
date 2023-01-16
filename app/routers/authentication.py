from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session 
from fastapi.security import OAuth2PasswordRequestForm

from app import models
from app.schemas.user import User, UserCreate, UserProfile
from app.utils.oauth2 import get_current_user
from app.database import get_db
from app.utils.security import verify_password, get_hashed_password, create_access_token

router = APIRouter(tags=['Authentication'])


@router.post('/signup', response_model=User)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == request.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    new_user = models.User(email=request.email, hashed_password=get_hashed_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=404,
            detail='Invalid credential'
        )
    access_token = create_access_token(
        data={'sub': user.email}
    )
    return {'access_token': access_token, 'token_type': 'bearer'}
