from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import pandas as pd

# 1. Initialize FastAPI app
app = FastAPI(
    title="Customer Churn Prediction API",
    description="API to predict if a telecommunications customer is at high risk of churning.",
    version="1.0.0"
)

# 2. Allow React frontend (port 5173) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load the trained model on startup
print("Loading model...")
model_pipeline = joblib.load('churn_model.joblib')
print("Model loaded successfully.")

# 3. Define the Input Schema using Pydantic
# This ensures that whoever calls our API sends the exact data types we expect.
class CustomerData(BaseModel):
    gender: str = Field(..., example="Female")
    SeniorCitizen: int = Field(..., example=0)
    Partner: str = Field(..., example="Yes")
    Dependents: str = Field(..., example="No")
    tenure: int = Field(..., example=1)
    PhoneService: str = Field(..., example="No")
    MultipleLines: str = Field(..., example="No phone service")
    InternetService: str = Field(..., example="DSL")
    OnlineSecurity: str = Field(..., example="No")
    OnlineBackup: str = Field(..., example="Yes")
    DeviceProtection: str = Field(..., example="No")
    TechSupport: str = Field(..., example="No")
    StreamingTV: str = Field(..., example="No")
    StreamingMovies: str = Field(..., example="No")
    Contract: str = Field(..., example="Month-to-month")
    PaperlessBilling: str = Field(..., example="Yes")
    PaymentMethod: str = Field(..., example="Electronic check")
    MonthlyCharges: float = Field(..., example=29.85)
    TotalCharges: float = Field(..., example=29.85) # Pydantic forces this to be a float!

# 4. Define the Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running and model is loaded."}

# 5. Define the Prediction Endpoint
@app.post("/predict")
def predict_churn(customer: CustomerData):
    try:
        # Convert the incoming JSON payload into a Pandas DataFrame
        # (Our Scikit-Learn pipeline expects a DataFrame with these column names)
        customer_df = pd.DataFrame([customer.model_dump()])
        
        # Make the prediction
        prediction = model_pipeline.predict(customer_df)
        probability = model_pipeline.predict_proba(customer_df)
        
        # prediction is an array like [1] or [0]
        is_churn = int(prediction[0])
        churn_probability = float(probability[0][1])
        
        return {
            "churn_prediction": "Yes" if is_churn == 1 else "No",
            "churn_probability": round(churn_probability, 4),
            "risk_level": "High" if churn_probability > 0.7 else ("Medium" if churn_probability > 0.4 else "Low")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
