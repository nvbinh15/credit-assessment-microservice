from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import User
from app import models
from app.database import get_db
from app.utils.oauth2 import get_current_user
from app.schemas.user import Profile, UserProfile


router = APIRouter(prefix='/profile', tags=['Profile'])


@router.put('', tags=['Profile'], response_model=Profile)
def update_profile(request: Profile, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_db = db.query(models.User).filter(models.User.id == current_user.id)
    if not user_db.first():
        raise HTTPException(status_code=404, detail='Not found')
    user_db.update(request.dict(exclude_unset=True))
    db.commit()
    db.refresh(user_db.first())
    return user_db.first()


@router.get('/me', response_model=UserProfile)
def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user