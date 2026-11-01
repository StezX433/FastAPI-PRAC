from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    age : int
    income : float
    loan_amount: float
    employeement_years: int
    
    
@app.post("/predict")
def predict_loan(application: LoanApplication):
    if application.income > 50000 and application.employeement_years > 2:
        decision = "Approved"
    else:
        decision = "Rejected"
        
    return {
        "age": application.age,
        "income": application.income,
        "loan_amount": application.loan_amount,
        "employeement_years": application.employeement_years,
        "decision": decision
    }
