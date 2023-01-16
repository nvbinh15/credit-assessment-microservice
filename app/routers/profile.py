from fastapi import APIRouter


router = APIRouter(prefix='/profile', tags=['Profile'])


@router.post('', tags=['Profile'])
def create_profile():
    pass 


@router.put('', tags=['Profile'])
def update_profile():
    pass 