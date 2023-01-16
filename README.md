# credit-assessment-microservice

## Inspiration

According to S&P Global market intelligence, Singapore's leading banks face slower loan growth in 2023, tied down by tight monetary policy and a poorer picture for Asia-Pacific economies as central banks keep their focus on inflation control (2022). Increases in interest rates since late 2021 have boosted Singapore's largest lenders by assets. However, this rise could become a double-edged sword, and hinder borrowing. We mainly target two objectives that also experience constraints in lending, which are individual consumers and small and medium-sized enterprises (SMEs). 

Singapore's current process of assessing and approving loans is not optimized, which creates obstacles for both borrowers and lenders. Given the problem's urgency and its consequences on economic development, our team believes that Machine Learning can be applied to simplify the loan application process and give users a holistic view of each other's credibility and capability.

## What it does

To address the aforementioned difficulties, we proposed a Loan Management and Credit Assessment Microservice. The API is beneficial to different stakeholders, including investors,  SMEs, and individual users. It complies with the OpenAPI standard and contains 2 main components:

- Public credit-assessment endpoints that are powered by machine learning models. Clients can use these endpoints to determine individuals' credit score buckets (Good, Standard, or Poor), prediction of whether a personal loan will be accepted or not, and expected loan amount for SMEs by using collateral analysis.

- Loan management component serves as the backend for a mobile application. We have also provided a Figma prototype for this application.

## How we built it

We use scikit-learn to build our machine learning models and FastAPI to build the microservice. 

## Challenges we ran into

How to find relevant datasets to build our model.

## What's next for Loan Management and Credit Assessment Microservice

As our Loan Management backend gets data from users, that data can be used to enhance our prediction model. For further improvement of our microservice, we can add an online learning component to train our models in real-time. 
