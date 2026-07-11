
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import Response
import os
import pandas as pd
import joblib
import time

from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST
)


# =====================================================
# Load Artifacts
# =====================================================

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")


# =====================================================
# Production Data Logging
# =====================================================

LOG_FILE = "production_logs.csv"


def log_prediction(df: pd.DataFrame):

    if os.path.exists(LOG_FILE):
        df.to_csv(
            LOG_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            LOG_FILE,
            index=False
        )


# =====================================================
# Prometheus Metrics
# =====================================================

prediction_requests = Counter(
    "prediction_requests_total",
    "Total number of prediction requests"
)

prediction_errors = Counter(
    "prediction_errors_total",
    "Total failed prediction requests"
)

prediction_latency = Histogram(
    "prediction_latency_seconds",
    "Prediction latency"
)


# =====================================================
# FastAPI
# =====================================================

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0"
)


# =====================================================
# Input Schema
# =====================================================

class Customer(BaseModel):

    Age: float
    Tenure: float
    Usage_Frequency: float
    Support_Calls: float
    Payment_Delay: float
    Total_Spend: float
    Last_Interaction: float

    Subscription_Type_Num: int
    Contract_Length_Num: int

    Avg_Spend_Per_Month: float
    Support_Calls_Per_Month: float
    Payment_Reliability: float
    Engagement_Score: float

    Tenure_Group_Num: int

    High_Support_Risk: int
    High_Payment_Risk: int
    Low_Usage_Risk: int


# =====================================================
# Health Endpoint
# =====================================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# =====================================================
# Prediction Endpoint
# =====================================================

@app.post("/predict")
def predict(customer: Customer):

    start_time = time.time()

    prediction_requests.inc()

    try:

        data = customer.model_dump()

        df = pd.DataFrame([{
            "Age": data["Age"],
            "Tenure": data["Tenure"],
            "Usage Frequency": data["Usage_Frequency"],
            "Support Calls": data["Support_Calls"],
            "Payment Delay": data["Payment_Delay"],
            "Total Spend": data["Total_Spend"],
            "Last Interaction": data["Last_Interaction"],
            "Subscription_Type_Num": data["Subscription_Type_Num"],
            "Contract_Length_Num": data["Contract_Length_Num"],
            "Avg_Spend_Per_Month": data["Avg_Spend_Per_Month"],
            "Support_Calls_Per_Month": data["Support_Calls_Per_Month"],
            "Payment_Reliability": data["Payment_Reliability"],
            "Engagement_Score": data["Engagement_Score"],
            "Tenure_Group_Num": data["Tenure_Group_Num"],
            "High_Support_Risk": data["High_Support_Risk"],
            "High_Payment_Risk": data["High_Payment_Risk"],
            "Low_Usage_Risk": data["Low_Usage_Risk"]
        }])

        log_prediction(df)

        df = df[feature_names]

        scaled = scaler.transform(df)

        prediction = model.predict(scaled)[0]

        probability = model.predict_proba(scaled)[0][1]

        prediction_latency.observe(
            time.time() - start_time
        )

        return {
            "prediction": int(prediction),
            "probability": round(
                float(probability),
                4
            )
        }

    except Exception as e:

        prediction_errors.inc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =====================================================
# Prometheus Metrics Endpoint
# =====================================================

@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
