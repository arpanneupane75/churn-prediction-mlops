# Infrastructure

## Overview

This document describes the infrastructure used to deploy, monitor, and maintain the Customer Churn Prediction MLOps system.

The application is deployed on a local Kubernetes cluster provided by Docker Desktop. The infrastructure is fully containerized using Docker and orchestrated using Kubernetes. Monitoring is implemented with Prometheus and Grafana, while GitHub Actions automates testing and deployment workflows.

The deployment architecture has been designed to remain compatible with Azure Kubernetes Service (AKS), allowing future cloud migration with minimal configuration changes.

---

# Infrastructure Overview

The deployed system consists of four independent services.

| Component      | Technology                  | Purpose                                                 |
| -------------- | --------------------------- | ------------------------------------------------------- |
| Prediction API | FastAPI                     | Serves customer churn predictions                       |
| Drift Monitor  | FastAPI + Prometheus Client | Calculates feature drift and exposes monitoring metrics |
| Prometheus     | Prometheus                  | Collects application and monitoring metrics             |
| Grafana        | Grafana                     | Visualizes operational dashboards                       |

---

# Infrastructure Architecture

```text
                     GitHub Repository
                            │
                            ▼
                    GitHub Actions (CI/CD)
                            │
                            ▼
                     Docker Image Build
                            │
                            ▼
                  Docker Desktop Kubernetes
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
  Prediction API      Drift Monitor       Prometheus
        │                   │                   │
        └───────────────────┴───────────────────┘
                            │
                            ▼
                        Grafana
```

---

# Kubernetes Resources

The application is deployed using Kubernetes Deployments and Services.

| Resource    |         Quantity | Description                                   |
| ----------- | ---------------: | --------------------------------------------- |
| Namespace   |                1 | Default namespace                             |
| Deployments |                4 | One deployment for each application component |
| Services    |                4 | Internal service discovery                    |
| Pods        |                4 | One pod per deployment                        |
| ReplicaSets |                4 | Automatically managed by Kubernetes           |
| Replicas    | 1 per deployment | Suitable for local development                |

The single replica configuration minimizes resource usage while demonstrating Kubernetes orchestration concepts. The deployment manifests can be scaled by increasing the replica count without modifying the application code.

---

# Prediction API

Deployment Name

```text
churn-api
```

Technology

* FastAPI
* Uvicorn
* Scikit-learn
* Joblib

Replica Count

```text
1
```

Container Port

```text
8000
```

Service Type

```text
ClusterIP
```

Responsibilities

* Load production artifacts
* Validate prediction requests
* Perform feature preprocessing
* Generate churn predictions
* Export Prometheus metrics
* Respond to health checks

Loaded Production Artifacts

* churn_model.pkl
* scaler.pkl
* feature_names.pkl
* baseline.json
* metadata.json

Health Checks

* Readiness Probe
* Liveness Probe

---

# Drift Monitoring Service

Deployment Name

```text
drift-monitor
```

Replica Count

```text
1
```

Container Port

```text
8001
```

Service Type

```text
ClusterIP
```

Responsibilities

* Read baseline statistics
* Compare incoming data with training distribution
* Calculate feature drift
* Export drift metrics
* Provide monitoring endpoint

Current Drift Metrics

* drift_age
* drift_tenure
* drift_usage_frequency
* drift_support_calls
* drift_payment_delay
* drift_total_spend
* drift_last_interaction

Additional features are automatically exported whenever baseline statistics are updated.

---

# Prometheus

Deployment Name

```text
prometheus
```

Replica Count

```text
1
```

Container Port

```text
9090
```

Responsibilities

* Collect application metrics
* Store time-series metrics
* Scrape monitoring endpoints
* Provide query interface

Scrape Targets

* Prediction API
* Drift Monitoring Service

Configuration File

```text
prometheus.yml
```

---

# Grafana

Deployment Name

```text
grafana
```

Replica Count

```text
1
```

Container Port

```text
3000
```

Responsibilities

* Connect to Prometheus
* Display operational dashboards
* Visualize system metrics
* Monitor application health

Current Dashboards

* Prediction Requests
* Prediction Errors
* Prediction Latency
* Feature Drift

---

# Docker Infrastructure

The application is containerized using Docker.

Current Images

| Image         | Purpose                    |
| ------------- | -------------------------- |
| churn-api     | FastAPI prediction service |
| churn-monitor | Drift monitoring service   |

Each image contains only the components required by its respective service, reducing unnecessary dependencies and improving maintainability.

---

# Networking

The Kubernetes Services provide internal communication between components.

| Component      | Service Port |
| -------------- | -----------: |
| Prediction API |         8000 |
| Drift Monitor  |         8001 |
| Prometheus     |         9090 |
| Grafana        |         3000 |

Service discovery is handled automatically by Kubernetes.

---

# Storage

The system stores production artifacts separately from the training pipeline.

Directory

```text
artifacts/
```

Contents

| Artifact          | Purpose                               |
| ----------------- | ------------------------------------- |
| churn_model.pkl   | Production machine learning model     |
| scaler.pkl        | Feature scaling                       |
| feature_names.pkl | Feature ordering                      |
| baseline.json     | Drift monitoring baseline             |
| metadata.json     | Model metadata and evaluation metrics |

Datasets are intentionally excluded from deployment containers because they are only required during model training.

---

# CI/CD Infrastructure

GitHub Actions automates software validation and deployment.

Continuous Integration

The CI workflow performs:

* Repository checkout
* Python environment setup
* Dependency installation
* Unit testing using Pytest
* Build validation

Continuous Deployment

The CD workflow is triggered only when the retraining pipeline updates production artifacts.

Deployment workflow:

1. Retraining pipeline completes.
2. Best model is compared with production.
3. Production artifacts are updated if the model improves.
4. Changes are committed automatically.
5. Changes are pushed to GitHub.
6. GitHub Actions builds the updated deployment.

The Kubernetes deployment configuration is maintained for future Azure Kubernetes Service (AKS) deployment.

---

# Resource Utilization

The current infrastructure is optimized for local development.

| Component      | Replicas |
| -------------- | -------: |
| Prediction API |        1 |
| Drift Monitor  |        1 |
| Prometheus     |        1 |
| Grafana        |        1 |

Total Running Pods

```text
4
```

This configuration minimizes resource consumption while preserving the complete production workflow.

---

# Production Characteristics

The deployed infrastructure provides:

* Containerized application deployment
* Kubernetes orchestration
* Health monitoring
* Automatic container recovery
* Centralized metrics collection
* Interactive dashboards
* Automated retraining support
* Automated CI/CD integration
* Production artifact management

The infrastructure closely resembles a cloud-native deployment and is designed for straightforward migration to Azure Kubernetes Service by replacing the local Kubernetes cluster with a managed AKS cluster.
