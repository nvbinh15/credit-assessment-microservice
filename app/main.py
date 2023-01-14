from fastapi import FastAPI
from .routers import user, loan
from . import models
from .database import engine

app = FastAPI()

app.include_router(user.router)
app.include_router(loan.router)

models.Base.metadata.create_all(engine)