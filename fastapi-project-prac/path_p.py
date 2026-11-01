from fastapi import FastAPI

app = FastAPI()

customer_risk_profiles = {
    1: {"name": "John Doe", "risk_profile": "Low"},
    2: {"name": "Jane Smith", "risk_profile": "Medium"},
    3: {"name": "Alice Johnson", "risk_profile": "High"},
}

@app.get("/customer")
def get_customer(city: str , state :str):
    return {
            "city": city,
            "state": state,
            "name": "John Doe",
    }

@app.get("/customer/{customer_id}")
def customer_risk_profile(customer_id: int):
    if customer_id in customer_risk_profiles:
        return customer_risk_profiles[customer_id]
    else:
        return {"error": "Customer not found"}
    
    
@app.get("/models/{model_name}/customer/{customer_id}")
def model_customer_risk_profile(model_name: str, customer_id: int):
    if customer_id in customer_risk_profiles:
        risk_profile = customer_risk_profiles[customer_id]
        return {
            "model_name": model_name,
            "customer_id": customer_id,
            "name": risk_profile["name"],
            "risk_profile": risk_profile["risk_profile"]
        }
    else:
        return {"error": f"Customer {customer_id} not found"}