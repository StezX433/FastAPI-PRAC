import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel , Field



app=FastAPI()
model = joblib.load("house_model.joblib")
features = joblib.load("house_features.joblib")


class HouseFeatures(BaseModel):
    MedInc: float = Field(gt=0, description="Median income in block group")
    HouseAge: float = Field(gt=0, description="Median house age in block group")
    AveRooms: float = Field(gt=0, description="Average number of rooms per household")
    AveBedrms: float = Field(gt=0, description="Average number of bedrooms per household")
    Population: float = Field(gt=0, description="Block group population")
    AveOccup: float = Field(gt=0, description="Average number of household members")
    Latitude: float = Field(ge=32,le=42, description="Block group latitude")
    Longitude: float = Field(ge=-125,le=-114, description="Block group longitude")
    
    
#home
@app.get("/")
def home():
    return {
        "message": "Welcome to the House Price Prediction API",
        "status": "success",
        "endpoint": "send post request to /predict"
}
    
@app.get("/health")
def health():
    return {
        "message": "API is healthy",
        "status": "success",
        "features": features,
        "avg_error" : "$39,300"
    }


@app.post("/predict")
def predict(house: HouseFeatures):
    try:
        input_data = pd.DataFrame([{
                "MedInc": house.MedInc,
                "HouseAge": house.HouseAge,
                "AveRooms": house.AveRooms,
                "AveBedrms": house.AveBedrms,
                "Population": house.Population,
                "AveOccup": house.AveOccup,
                "Latitude": house.Latitude,
                "Longitude": house.Longitude
        }])

        predicted = model.predict(input_data)[0]
        price_usd = predicted * 100000

        return {
            "predicted_price": f"${price_usd:,.0f}",
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"prediction failed: {str(e)}"
        )