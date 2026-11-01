from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    loan_amount: float
    employeement_years: int
    
@app.post("/predict")
def predict_loan(application: LoanApplication):
    #model logic here
    
    approved = (
        application.income > 50000 and application.employeement_years > 2
    )
    
    return {
        "name": application.name,
        "age": application.age,
        "income": application.income,
        "loan_amount": application.loan_amount,
        "employeement_years": application.employeement_years,
        "decision": "approved" if approved else "rejected"
    }
    