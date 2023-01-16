from fastapi import FastAPI
from app.routers import authentication, profile, loan, credit
from app import models
from app.database import engine

app = FastAPI(
    title="CreditAPI",
    description="Loan management and credit assessment microservice \
        powered by machine learning models"
)

app.include_router(credit.router)
app.include_router(authentication.router)
app.include_router(profile.router)
app.include_router(loan.router)

models.Base.metadata.create_all(engine)