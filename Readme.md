# 🚀 Customer Churn Prediction MLOps Pipeline

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-F46800?logo=grafana)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-0194E2)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?logo=githubactions)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble-success)

---

# Table of Contents

* [Project Overview](#project-overview)
* [Key Features](#key-features)
* [Demo](#demo)
* [System Architecture](#system-architecture)
* [Repository Structure](#repository-structure)
* [Project Documentation](#project-documentation)
* [Technology Stack](#technology-stack)
* [Dataset](#dataset)
* [Model Performance](#model-performance)
* [Installation](#installation)
* [Local Development](#local-development)
* [Docker Deployment](#docker-deployment)
* [Kubernetes Deployment](#kubernetes-deployment)
* [Monitoring](#monitoring)
* [REST API](#rest-api)
* [Automated Retraining Pipeline](#automated-retraining-pipeline)
* [CI/CD Pipeline](#cicd-pipeline)
* [Project Workflow](#project-workflow)
* [Screenshots](#screenshots)
* [Future Improvements](#future-improvements)
* [Contributing](#contributing)
* [License](#license)
* [Author](#author)

---

# Project Overview

This project demonstrates an end-to-end **production-ready Machine Learning Operations (MLOps) pipeline** for customer churn prediction.

Unlike a traditional machine learning project, this repository implements the complete lifecycle of a production ML system, including:

* Data preprocessing
* Feature engineering
* Model training
* Model comparison
* Automated artifact management
* FastAPI model serving
* Docker containerization
* Kubernetes deployment
* Prometheus monitoring
* Grafana dashboards
* Data drift detection
* Automated retraining
* GitHub Actions CI/CD

The objective is to simulate how machine learning models are developed, deployed, monitored, and continuously improved in a real production environment.

---

# Key Features

✅ End-to-End MLOps Pipeline

✅ Automated Feature Engineering

✅ Multi-model Training

* Logistic Regression
* Random Forest
* Gradient Boosting
* XGBoost

✅ Automatic Best Model Selection

✅ Production Model Comparison

✅ Automatic Artifact Versioning

✅ FastAPI REST API

✅ Dockerized Application

✅ Kubernetes Deployment

✅ Prometheus Metrics

✅ Grafana Dashboard

✅ Data Drift Monitoring

✅ Automated Retraining Pipeline

✅ GitHub Actions CI

✅ Automated CD Trigger after Successful Retraining

---

# Demo

## API Demo

> **Placeholder**

```
docs/demo/api_demo.gif
```

---

## Kubernetes Deployment

> **Placeholder**

```
docs/demo/kubernetes_demo.gif
```

---

## Grafana Dashboard

> **Placeholder**

```
docs/screenshots/grafana_dashboard.png
```

---

## Prometheus Metrics

> **Placeholder**

```
docs/screenshots/prometheus_metrics.png
```

---

## Drift Monitoring

> **Placeholder**

```
docs/screenshots/drift_dashboard.png
```

---

# System Architecture

Insert the exported image from:

```
docs/diagrams/system_architecture.drawio
```

Example:

```markdown
![System Architecture](docs/diagrams/system_architecture.png)
```

---

# Repository Structure

```text
Customer_Churn_MLOps/
│
├── app.py
├── train.py
├── monitor.py
├── requirements.txt
├── Dockerfile
├── Dockerfile.monitor
├── docker-compose.yml
├── prometheus.yml
│
├── artifacts/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   ├── baseline.json
│   └── metadata.json
│
├── automation/
│
├── retraining/
│
├── tests/
│
├── k8s/
│
├── docs/
│
├── .github/
│
└── README.md
```

---

# Project Documentation

## Core Documentation

| Document             | Description                         |
| -------------------- | ----------------------------------- |
| architecture.md      | Overall software architecture       |
| infrastructure.md    | Deployment infrastructure           |
| project_structure.md | Repository explanation              |
| api.md               | REST API reference                  |
| monitoring.md        | Monitoring architecture             |
| ci_cd.md             | Continuous Integration & Deployment |
| retraining.md        | Automated retraining workflow       |

---

## Architecture Decision Records (ADR)

| ADR     | Description                   |
| ------- | ----------------------------- |
| ADR-001 | Modular Architecture          |
| ADR-002 | Model Selection Strategy      |
| ADR-003 | Docker Containerization       |
| ADR-004 | Kubernetes Deployment         |
| ADR-005 | Monitoring Stack              |
| ADR-006 | Automated Retraining Pipeline |

---

## Draw.io Diagrams

| Diagram                 |
| ----------------------- |
| System Architecture     |
| Modular Architecture    |
| Training Pipeline       |
| Model Selection         |
| Docker Architecture     |
| Kubernetes Architecture |
| Monitoring Architecture |
| Retraining Pipeline     |
| CI/CD Pipeline          |
| API Request Flow        |

---

# Technology Stack

## Programming

* Python 3.13

## Machine Learning

* Scikit-learn
* XGBoost
* Pandas
* NumPy

## API

* FastAPI
* Uvicorn

## Monitoring

* Prometheus
* Grafana

## Containerization

* Docker

## Orchestration

* Kubernetes

## Experiment Tracking

* MLflow

## CI/CD

* GitHub Actions

## Version Control

* Git
* GitHub

---

# Project Highlights

* Production-style repository structure
* Modular Python implementation
* Multiple ML algorithms
* Automated model comparison
* Feature engineering pipeline
* Versioned artifacts
* Monitoring-ready REST API
* Drift detection
* Automatic retraining
* Kubernetes deployment
* Continuous Integration
* Continuous Deployment
* Extensive project documentation
* Architecture Decision Records
* Professional Draw.io architecture diagrams

---

# Dataset

**Problem**

Predict whether a telecom customer will churn based on demographic and usage behavior.

**Features include**

* Age
* Gender
* Tenure
* Usage Frequency
* Support Calls
* Payment Delay
* Subscription Type
* Contract Length
* Total Spend
* Last Interaction

Target Variable

```
Churn
```

---

# Model Performance

| Model               | Accuracy    | Precision   | Recall      | F1 Score    | ROC-AUC     |
| ------------------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Logistic Regression | Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Random Forest       | Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Gradient Boosting   | Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| XGBoost             | Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |

> These values can be updated after the latest training run.

---

# Installation

## Prerequisites

Ensure the following software is installed before running the project.

| Software                    | Version     |
| --------------------------- | ----------- |
| Python                      | 3.13+       |
| Git                         | Latest      |
| Docker Desktop              | Latest      |
| Kubernetes (Docker Desktop) | Enabled     |
| Prometheus                  | v3.x        |
| Grafana                     | Latest      |
| VS Code                     | Recommended |

---

# Clone the Repository

```bash
git clone https://github.com/<your-username>/customer-churn-mlops.git

cd customer-churn-mlops
```

---

# Create a Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

# Project Configuration

The project expects the following directory structure.

```text
artifacts/
    churn_model.pkl
    scaler.pkl
    feature_names.pkl
    baseline.json
    metadata.json

data/
    train_data.csv
    test_data.csv
```

---

# Training the Initial Model

Train all machine learning models.

```bash
python train.py
```

During training the pipeline performs:

* Dataset loading
* Feature engineering
* Data preprocessing
* Feature scaling
* Model training
* Model evaluation
* Best model selection
* MLflow experiment logging
* Artifact generation

Generated artifacts:

```text
artifacts/

churn_model.pkl

scaler.pkl

feature_names.pkl

baseline.json

metadata.json
```

---

# Running the FastAPI Server

Start the prediction API.

```bash
uvicorn app:app --reload
```

Server URL

```text
http://127.0.0.1:8000
```

Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```text
http://127.0.0.1:8000/redoc
```

---

# Running the Drift Monitor

The drift monitor exposes Prometheus metrics describing feature drift.

```bash
python monitor.py
```

Default Endpoint

```text
http://localhost:8001/metrics
```

---

# Running the Retraining Pipeline

The retraining pipeline automatically:

* Loads updated data
* Performs feature engineering
* Retrains all models
* Evaluates performance
* Compares against production
* Updates artifacts if performance improves
* Commits updated artifacts
* Pushes to GitHub
* Triggers GitHub Actions

Run

```bash
python -m retraining.retraining_pipeline
```

---

# Docker Deployment

## Build API Image

```bash
docker build -t churn-api:latest .
```

---

## Build Drift Monitor

```bash
docker build -f Dockerfile.monitor -t churn-monitor:latest .
```

---

## Verify Images

```bash
docker images
```

Expected Output

```text
churn-api

churn-monitor
```

---

## Run API Container

```bash
docker run -p 8000:8000 churn-api:latest
```

---

## Run Drift Monitor

```bash
docker run -p 8001:8001 churn-monitor:latest
```

---

# Kubernetes Deployment

Enable Kubernetes from Docker Desktop before deployment.

---

## Deploy API

```bash
kubectl apply -f k8s/api-deployment.yaml

kubectl apply -f k8s/api-service.yaml
```

---

## Deploy Drift Monitor

```bash
kubectl apply -f k8s/drift-monitor-deployment.yaml

kubectl apply -f k8s/drift-monitor-service.yaml
```

---

## Deploy Prometheus

```bash
kubectl apply -f k8s/prometheus-deployment.yaml

kubectl apply -f k8s/prometheus-service.yaml
```

---

## Deploy Grafana

```bash
kubectl apply -f k8s/grafana-deployment.yaml

kubectl apply -f k8s/grafana-service.yaml
```

---

## Verify Pods

```bash
kubectl get pods
```

Example

```text
NAME                READY

churn-api           1/1

drift-monitor       1/1

prometheus          1/1

grafana             1/1
```

---

## Verify Services

```bash
kubectl get svc
```

---

## Kubernetes Dashboard Screenshot

> Placeholder

```text
docs/screenshots/kubernetes_pods.png
```

---

# Monitoring

The project uses Prometheus for metric collection and Grafana for visualization.

---

## Prometheus

Available metrics include

* prediction_requests_total
* prediction_errors_total
* prediction_latency_seconds
* drift_age
* drift_total_spend
* drift_usage_frequency
* drift_support_calls
* drift_payment_delay

Prometheus URL

```text
http://localhost:9090
```

Screenshot Placeholder

```text
docs/screenshots/prometheus_dashboard.png
```

---

## Grafana

Grafana dashboards visualize

* Prediction traffic
* API latency
* Error rate
* Feature drift
* Request volume
* System health

Default URL

```text
http://localhost:3000
```

Screenshot Placeholder

```text
docs/screenshots/grafana_dashboard.png
```

---

# REST API

## Health Check

```http
GET /health
```

Example Response

```json
{
  "status": "healthy"
}
```

---

## Prediction Endpoint

```http
POST /predict
```

Example Request

```json
{
  "Age": 45,
  "Gender": "Male",
  "Tenure": 24,
  "Usage Frequency": 15,
  "Support Calls": 1,
  "Payment Delay": 0,
  "Subscription Type": "Premium",
  "Contract Length": "Annual",
  "Total Spend": 520,
  "Last Interaction": 12
}
```

Example Response

```json
{
  "prediction": 0,
  "probability": 0.94
}
```

---

## Metrics Endpoint

```http
GET /metrics
```

Used by

* Prometheus
* Grafana
* Drift Monitoring

---

# Documentation

For detailed explanations of each component, refer to the documentation below.

| Document            | Link                      |
| ------------------- | ------------------------- |
| Architecture        | docs/architecture.md      |
| Infrastructure      | docs/infrastructure.md    |
| Project Structure   | docs/project_structure.md |
| Monitoring          | docs/monitoring.md        |
| REST API            | docs/api.md               |
| Retraining Pipeline | docs/retraining.md        |
| CI/CD               | docs/ci_cd.md             |
| ADR                 | docs/adr/                 |
| Draw.io Diagrams    | docs/diagrams/            |

---

# Automated Retraining Pipeline

The project includes an automated retraining pipeline that continuously evaluates newly trained models against the current production model.

Rather than replacing the deployed model after every training run, the pipeline only promotes a new model when it demonstrates a meaningful performance improvement.

## Pipeline Overview

1. Load the latest training and testing datasets.
2. Perform feature engineering.
3. Preprocess and scale the data.
4. Train multiple machine learning models.
5. Evaluate each model using several performance metrics.
6. Select the best-performing model based on the F1 Score.
7. Compare the best retrained model against the current production model.
8. If the new model exceeds the minimum improvement threshold:

   * Update production artifacts.
   * Generate new metadata.
   * Commit the updated artifacts.
   * Push changes to GitHub.
   * Trigger the GitHub Actions CI/CD workflow.
9. Otherwise, retain the existing production model.

---

## Retraining Workflow

Insert the exported diagram here.

```text
docs/diagrams/retraining_pipeline.png
```

```markdown
![Retraining Pipeline](docs/diagrams/retraining_pipeline.png)
```

---

## Model Comparison Strategy

The pipeline compares the following metrics for both the production and retrained models:

| Metric    | Purpose                            |
| --------- | ---------------------------------- |
| Accuracy  | Overall classification performance |
| Precision | False positive control             |
| Recall    | False negative control             |
| F1 Score  | Primary deployment metric          |
| ROC-AUC   | Overall classifier discrimination  |

The deployment decision is based on the F1 Score.

If the improvement is less than the configured threshold, the existing production model is retained.

---

## Generated Production Artifacts

Whenever a better model is identified, the following artifacts are regenerated.

```text
artifacts/

├── churn_model.pkl
├── scaler.pkl
├── feature_names.pkl
├── baseline.json
└── metadata.json
```

The metadata file contains:

* Model name
* Training timestamp
* Performance metrics
* Feature count

---

# Continuous Integration / Continuous Deployment

The project uses GitHub Actions to automate validation and deployment.

The CI workflow executes after every push to the main branch.

The CD workflow executes after a successful CI run and publishes updated production artifacts.

---

## Continuous Integration

The CI workflow performs the following tasks:

* Checkout repository
* Configure Python
* Install dependencies
* Run unit tests
* Verify project imports
* Validate training pipeline
* Ensure artifacts are correctly generated

Workflow file

```text
.github/workflows/ci.yml
```

---

## Continuous Deployment

The CD workflow executes only after a successful CI pipeline.

Current deployment steps include:

* Checkout repository
* Build Docker image
* Publish Docker image to GitHub Container Registry
* Prepare deployment for Kubernetes
* Ready for Azure Kubernetes Service integration

Workflow file

```text
.github/workflows/cd.yml
```

---

## CI/CD Workflow

Insert the exported diagram.

```text
docs/diagrams/ci_cd_pipeline.png
```

```markdown
![CI/CD Pipeline](docs/diagrams/ci_cd_pipeline.png)
```

---

# Complete Project Workflow

The following diagram illustrates the complete lifecycle implemented in this repository.

```text
Dataset
      │
      ▼
Feature Engineering
      │
      ▼
Preprocessing
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
Artifact Generation
      │
      ▼
FastAPI Deployment
      │
      ▼
Docker Container
      │
      ▼
Kubernetes Deployment
      │
      ▼
Prediction API
      │
      ▼
Prometheus Metrics
      │
      ▼
Grafana Dashboard
      │
      ▼
Data Drift Detection
      │
      ▼
Retraining Pipeline
      │
      ▼
GitHub Actions
      │
      ▼
Updated Production Model
```

Insert the workflow diagram.

```text
docs/diagrams/system_architecture.png
```

---

# Project Screenshots

## Repository Structure

> Placeholder

```text
docs/screenshots/repository_structure.png
```

---

## Swagger UI

> Placeholder

```text
docs/screenshots/swagger_ui.png
```

---

## FastAPI Prediction

> Placeholder

```text
docs/screenshots/prediction_api.png
```

---

## Docker Containers

> Placeholder

```text
docs/screenshots/docker_containers.png
```

---

## Kubernetes Pods

> Placeholder

```text
docs/screenshots/kubernetes_pods.png
```

---

## Kubernetes Services

> Placeholder

```text
docs/screenshots/kubernetes_services.png
```

---

## Prometheus Dashboard

> Placeholder

```text
docs/screenshots/prometheus_dashboard.png
```

---

## Grafana Dashboard

> Placeholder

```text
docs/screenshots/grafana_dashboard.png
```

---

## MLflow Experiment Tracking

> Placeholder

```text
docs/screenshots/mlflow_dashboard.png
```

---

## Drift Monitoring

> Placeholder

```text
docs/screenshots/drift_monitoring.png
```

---

# Performance Summary

| Model               |    Accuracy |   Precision |      Recall |    F1 Score |     ROC-AUC |
| ------------------- | ----------: | ----------: | ----------: | ----------: | ----------: |
| Logistic Regression | Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Random Forest       | Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Gradient Boosting   | Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| XGBoost             | Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |

---

# Testing

The repository includes automated tests covering the major application components.

Current test coverage includes:

* API health endpoint
* Prediction endpoint
* Metrics endpoint
* Artifact validation
* Model loading
* Pipeline verification

Run all tests using:

```bash
pytest
```

---

# Benchmark

Current implementation provides:

* Automated feature engineering
* Four machine learning models
* Automated model comparison
* Production artifact versioning
* REST API inference
* Docker containerization
* Kubernetes orchestration
* Prometheus monitoring
* Grafana visualization
* Drift detection
* Automated retraining
* GitHub Actions CI/CD

This architecture closely resembles a production-ready MLOps deployment while remaining suitable for local development and future cloud deployment.

---
# Future Improvements

The current implementation provides a complete local MLOps workflow. Future enhancements will focus on improving scalability, automation, and cloud-native deployment.

## Planned Improvements

### Cloud Deployment

* Deploy the application on Azure Kubernetes Service (AKS)
* Configure Azure Container Registry (ACR)
* Automate Kubernetes deployments from GitHub Actions
* Enable horizontal pod autoscaling

---

### Model Registry

* Integrate the MLflow Model Registry
* Maintain versioned production, staging, and archived models
* Enable rollback to previous model versions

---

### Data Versioning

* Integrate DVC (Data Version Control)
* Version training datasets
* Track dataset lineage across retraining cycles

---

### Advanced Monitoring

* Detect prediction drift
* Detect concept drift
* Monitor model confidence
* Create alerting rules for production failures
* Integrate Alertmanager

---

### Security

* JWT Authentication
* HTTPS/TLS
* Secrets Management
* Role-Based Access Control (RBAC)

---

### Scalability

* Multiple API replicas
* Horizontal Pod Autoscaler (HPA)
* Rolling updates
* Zero-downtime deployment
* Load balancing using Kubernetes Services

---

### Logging

* Centralized log aggregation
* Structured logging
* ELK or Loki integration
* Request tracing

---

# Project Statistics

| Category                      | Value                |
| ----------------------------- | -------------------- |
| Programming Language          | Python               |
| ML Algorithms                 | 4                    |
| REST API                      | FastAPI              |
| Monitoring Stack              | Prometheus + Grafana |
| Containerization              | Docker               |
| Orchestration                 | Kubernetes           |
| Experiment Tracking           | MLflow               |
| CI/CD                         | GitHub Actions       |
| Automated Retraining          | Yes                  |
| Drift Detection               | Yes                  |
| Automated Artifact Versioning | Yes                  |
| Documentation                 | Extensive            |
| Architecture Diagrams         | 10                   |
| Architecture Decision Records | 6                    |

---

# Documentation Index

## Core Documentation

| File                        | Description                           |
| --------------------------- | ------------------------------------- |
| `docs/architecture.md`      | Overall system architecture           |
| `docs/project_structure.md` | Repository organization               |
| `docs/infrastructure.md`    | Deployment infrastructure             |
| `docs/api.md`               | REST API reference                    |
| `docs/monitoring.md`        | Monitoring architecture               |
| `docs/retraining.md`        | Automated retraining workflow         |
| `docs/ci_cd.md`             | Continuous Integration and Deployment |

---

## Architecture Decision Records

| ADR     | Description                   |
| ------- | ----------------------------- |
| ADR-001 | Modular Project Architecture  |
| ADR-002 | Model Selection Strategy      |
| ADR-003 | Docker Containerization       |
| ADR-004 | Kubernetes Deployment         |
| ADR-005 | Monitoring Architecture       |
| ADR-006 | Automated Retraining Pipeline |

---

## Architecture Diagrams

| Diagram                  |
| ------------------------ |
| System Architecture      |
| Modular Architecture     |
| Training Pipeline        |
| Model Selection Workflow |
| Docker Architecture      |
| Kubernetes Architecture  |
| Monitoring Architecture  |
| Retraining Pipeline      |
| CI/CD Pipeline           |
| API Request Flow         |

---

# Contributing

Contributions are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

Please ensure that:

* Code follows the existing project structure.
* Tests pass successfully.
* Documentation is updated when required.

---

# License

This project is released under the **MIT License**.

See the `LICENSE` file for complete license information.

---

# Acknowledgements

This project was developed using several open-source technologies.

* Python
* FastAPI
* Scikit-learn
* XGBoost
* MLflow
* Docker
* Kubernetes
* Prometheus
* Grafana
* GitHub Actions
* Pandas
* NumPy

Special thanks to the maintainers and contributors of these projects for providing excellent open-source tools that make production-grade machine learning systems possible.

---

# Author

**Arpan Neupane**

Computer Engineering Graduate
Machine Learning Engineer | MLOps Enthusiast | AI Developer

## Connect

* GitHub: https://github.com/arpanneupane75
* LinkedIn:https://www.linkedin.com/in/arpanneupane75
* Email:https://arpanneupane75@gmail.com

---

# Project Status

> **Current Status:** Active Development

### Completed

* End-to-End Machine Learning Pipeline
* Feature Engineering
* Data Preprocessing
* Multi-Model Training
* Model Evaluation
* Automated Best Model Selection
* FastAPI Inference API
* Docker Containerization
* Kubernetes Deployment
* Prometheus Monitoring
* Grafana Dashboards
* Drift Detection
* Automated Retraining Pipeline
* GitHub Actions CI
* Automated CD Workflow
* Comprehensive Documentation
* Architecture Decision Records
* Professional Architecture Diagrams

### In Progress

* Azure Kubernetes Service (AKS) Deployment
* Azure Container Registry (ACR) Integration
* Cloud-Native Production Deployment

---

# Repository Overview

This repository demonstrates how a traditional machine learning model can be transformed into a production-ready system by incorporating modern MLOps practices, including containerization, orchestration, monitoring, automated retraining, and CI/CD. It serves as both a learning resource and a reference implementation for deploying machine learning applications using industry-standard tools and workflows.

