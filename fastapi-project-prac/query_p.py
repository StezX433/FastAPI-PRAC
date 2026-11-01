from fastapi import FastAPI

app = FastAPI()

all_customers = [
     {"id": 1, "name": "John Doe", "city": "New York", "risk_profile": "Low"},
     {"id": 2, "name": "Jane Smith", "city": "Los Angeles", "risk_profile": "Medium"},
     {"id": 3, "name": "Alice Johnson", "city": "Chicago", "risk_profile": "High"},
     {"id": 4, "name": "Bob Brown", "city": "Houston", "risk_profile": "Low"},
     {"id": 5, "name": "Charlie Davis", "city": "Phoenix", "risk_profile": "Medium"}
]


@app.get("/customers")
def get_customers(city: str , risk_profile: str ):
    filtered = [
        c for c in all_customers
        if c["city"]==city and c["risk_profile"]==risk_profile
    ]
    
    return {
        "city": city,
        "risk_profile": risk_profile,
        "count": len(filtered)
    }