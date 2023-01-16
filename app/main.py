from fastapi import FastAPI
from .routers import authentication, profile, loan, credit
from . import models
from .database import engine

app = FastAPI()

app.include_router(credit.router)
app.include_router(authentication.router)
app.include_router(profile.router)
app.include_router(loan.router)

models.Base.metadata.create_all(engine)