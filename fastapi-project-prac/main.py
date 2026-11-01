from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/about")
def about():
    return {
            "location": "This is a FastAPI application created for practice purposes.",
            "version": "1.0.0",
            "author": "Kshitij"
            }
    
@app.get("/customer")
def get_customer(customer_id: int):
    return {
            "customer_id": customer_id,
            "name": "John Doe",
            "email": "john.doe@example.com"
            }