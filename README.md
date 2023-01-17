# credit-assessment-microservice

A loan management and credit assessment microservice powered by machine learning models. [Demo](https://youtu.be/94TqgqP3vDY)

Deployment: [http://18.142.225.55:8000/docs](http://18.142.225.55:8000/docs)

## Features

Public-available API endpoints:
- Credit assessment: classify user’s credit score into 3 different groups: Good, Standard, and Poor based on customers’ information
- Loan prediction: predict whether a personal loan will be accepted or not 
- SME loan estimation: calculate the amount of expected loan that SMEs will receive based on market-standard collateral analysis

Loan management API: serves as the backend for a loan management mobile application.

## Getting started

- Create and activate a virtual environment
- Install dependencies: `$ pip install -r requirements.txt`
- Create an environment file `app/.env` with a `SECRET_KEY` and activate the file by `$ source app/.env`
- Start the microservice: `uvicorn app.main:app --reload`
