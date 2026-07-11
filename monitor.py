import json
import pandas as pd

from fastapi import FastAPI
from fastapi.responses import Response

from prometheus_client import (
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST
)

# =====================================================
# FastAPI
# =====================================================

app = FastAPI(
    title="Customer Churn Drift Monitor",
    version="1.0"
)

# =====================================================
# Load Baseline
# =====================================================

with open("baseline.json", "r") as f:
    baseline = json.load(f)

# =====================================================
# Prometheus Gauges
# =====================================================

overall_drift = Gauge(
    "overall_data_drift",
    "Overall Data Drift Score"
)

feature_gauges = {}

for feature in baseline.keys():

    feature_gauges[feature] = Gauge(
        f"drift_{feature.lower().replace(' ', '_')}",
        f"Drift for {feature}"
    )

# =====================================================
# Drift Calculation
# =====================================================

def calculate_drift():

    try:
        production = pd.read_csv("production_logs.csv")

    except FileNotFoundError:
        return {
            "message": "No production data available yet."
        }

    total_drift = 0
    feature_count = 0

    drift_report = {}

    for feature in baseline.keys():

        if feature not in production.columns:
            continue

        train_mean = baseline[feature]["mean"]
        prod_mean = production[feature].mean()

        drift_value = abs(prod_mean - train_mean)

        # Update Prometheus Gauge
        feature_gauges[feature].set(drift_value)

        drift_report[feature] = round(drift_value, 4)

        total_drift += drift_value
        feature_count += 1

    if feature_count > 0:
        overall = total_drift / feature_count
    else:
        overall = 0

    overall_drift.set(overall)

    drift_report["overall_drift"] = round(overall, 4)

    return drift_report

# =====================================================
# Drift Endpoint
# =====================================================

@app.get("/drift")
def drift():

    return calculate_drift()

# =====================================================
# Prometheus Endpoint
# =====================================================

@app.get("/metrics")
def metrics():

    # Automatically refresh drift every scrape
    calculate_drift()

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

# =====================================================
# Health Check
# =====================================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }