# Monitoring

## Overview

Monitoring is an essential component of any production Machine Learning system. Beyond serving predictions, an MLOps application must continuously observe application health, system performance, and changes in incoming data that may affect model quality.

This project integrates Prometheus and Grafana to provide real-time observability while implementing feature drift monitoring to detect changes in production data distributions.

---

# Monitoring Architecture

The monitoring workflow is illustrated below.

```text
FastAPI API
     │
     ├──────────────► Prometheus Metrics
     │
     ▼
Prediction Requests
     │
     ▼
Feature Drift Monitor
     │
     ▼
Prometheus
     │
     ▼
Grafana Dashboards
```

---

# Monitoring Components

## FastAPI Metrics

The prediction service exposes a `/metrics` endpoint that is periodically scraped by Prometheus.

Metrics are generated for every prediction request without affecting application performance.

---

## Drift Monitoring Service

A dedicated monitoring service evaluates incoming production data against baseline statistics generated during training.

The service compares feature distributions with historical values stored inside `baseline.json`.

Feature statistics monitored include:

* Mean
* Standard deviation
* Minimum value
* Maximum value

Significant deviations may indicate data drift that could reduce model performance.

---

## Prometheus

Prometheus continuously collects metrics from both the FastAPI application and the drift monitoring service.

Responsibilities include:

* Time-series metric collection
* Metric storage
* Query processing
* Alert integration
* Historical performance tracking

The scrape configuration is defined within `prometheus.yml`.

---

## Grafana

Grafana connects directly to Prometheus and visualizes collected metrics through dashboards.

Typical dashboards include:

* Prediction throughput
* API latency
* Prediction errors
* Feature drift
* Service availability

Grafana enables operational monitoring without directly accessing application logs.

---

# Application Metrics

The FastAPI service exposes the following operational metrics.

| Metric                     | Type      | Description                         |
| -------------------------- | --------- | ----------------------------------- |
| prediction_requests_total  | Counter   | Total prediction requests processed |
| prediction_errors_total    | Counter   | Total failed prediction requests    |
| prediction_latency_seconds | Histogram | Prediction response latency         |

These metrics provide insight into application usage and performance.

---

# Drift Metrics

The monitoring service exports feature-level drift metrics.

Examples include:

* drift_age
* drift_tenure
* drift_usage_frequency
* drift_total_spend
* drift_payment_delay

Each metric represents the deviation between production data and baseline statistics generated during training.

These metrics help identify changes in customer behavior that may require model retraining.

---

# Monitoring Workflow

The monitoring process follows these steps:

1. Client sends prediction request.
2. FastAPI processes the request.
3. Prometheus metrics are updated.
4. Drift monitoring evaluates production features.
5. Metrics are exported.
6. Prometheus collects metrics.
7. Grafana visualizes dashboards.

This workflow provides continuous visibility into application health and model behavior.

---

# Health Monitoring

The application exposes a `/health` endpoint for readiness and liveness verification.

Kubernetes periodically checks this endpoint to determine whether the application is healthy.

Benefits include:

* Automatic recovery
* Failed container detection
* Self-healing deployments
* High availability

---

# Monitoring Objectives

The monitoring system is designed to answer the following operational questions:

* Is the API currently available?
* How many prediction requests are being processed?
* Is prediction latency increasing?
* Are prediction failures occurring?
* Has production data drifted from the training distribution?
* Should the model be retrained?

---

# Current Limitations

The current monitoring implementation focuses on application health and feature drift.

Future improvements include:

* Population Stability Index (PSI)
* Statistical drift tests
* Prediction confidence monitoring
* Model performance monitoring using labeled production data
* Automated alerting
* Distributed tracing
* Centralized logging

---

# Benefits

The monitoring architecture provides:

* Real-time operational visibility
* Early detection of data drift
* Performance monitoring
* Improved system reliability
* Support for proactive model maintenance

Together, Prometheus and Grafana provide a lightweight yet effective monitoring solution suitable for modern MLOps deployments.
