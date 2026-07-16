# Project Structure

This document describes the organization of the Customer Churn Prediction MLOps repository. The project follows a modular architecture, separating responsibilities across data processing, model training, deployment, monitoring, testing, and automation. This structure improves maintainability, scalability, and collaboration.

---

# Repository Structure

```text
Churn_prediction/
│
├── app.py
├── train.py
├── requirements.txt
├── Dockerfile
├── Dockerfile.monitor
├── docker-compose.yml
├── prometheus.yml
├── mlflow.db
│
├── artifacts/
├── automation/
├── data/
├── docs/
├── k8s/
├── logs/
├── mlruns/
├── monitoring/
├── retraining/
├── tests/
│
├── .github/
│   └── workflows/
│
└── README.md
```

---

# Root Files

## app.py

Implements the FastAPI application used for serving the production machine learning model. The API exposes prediction, health check, and Prometheus metrics endpoints.

Responsibilities:

* Load production artifacts
* Accept prediction requests
* Return churn predictions
* Record Prometheus metrics
* Provide health status

---

## train.py

Executes the initial model training workflow.

Responsibilities:

* Load datasets
* Perform preprocessing
* Train multiple machine learning models
* Evaluate model performance
* Register experiments using MLflow
* Produce initial production artifacts

---

## requirements.txt

Lists all Python dependencies required to execute the project.

Examples include:

* FastAPI
* Scikit-learn
* XGBoost
* Pandas
* NumPy
* MLflow
* Prometheus Client
* Pytest

---

## Dockerfile

Defines the Docker image used for the prediction API.

The Docker image installs project dependencies, copies the application code, and starts the FastAPI server.

---

## Dockerfile.monitor

Builds the monitoring service responsible for exposing feature drift metrics to Prometheus.

---

## docker-compose.yml

Defines a local multi-container environment for development.

It can be used to start:

* FastAPI
* Prometheus
* Grafana

using a single command.

---

## prometheus.yml

Contains the Prometheus scrape configuration.

Defines:

* Metrics endpoints
* Collection intervals
* Monitoring targets

---

## README.md

Provides an overview of the repository including installation instructions, architecture diagrams, deployment procedures, and project documentation.

---

# Directories

## artifacts/

Stores all production model artifacts generated during training or retraining.

Typical contents include:

```text
artifacts/
│
├── churn_model.pkl
├── scaler.pkl
├── feature_names.pkl
├── baseline.json
└── metadata.json
```

Purpose:

* Production model
* Feature scaler
* Feature list
* Baseline statistics
* Model metadata

These files are loaded by the FastAPI service during inference.

---

## automation/

Contains automation logic supporting continuous deployment.

Typical files:

```text
automation/
│
├── compare_models.py
└── deploy.py
```

Responsibilities:

* Compare production and retrained models
* Decide whether deployment should occur
* Commit updated artifacts
* Push changes to GitHub
* Trigger GitHub Actions

---

## data/

Contains datasets used for model development.

Typical structure:

```text
data/
│
├── train_data.csv
└── test_data.csv
```

These datasets are used exclusively for training and evaluation and are not included inside production Docker images.

---

## docs/

Contains all technical documentation describing the system.

Structure:

```text
docs/
│
├── architecture.md
├── deployment.md
├── monitoring.md
├── retraining_pipeline.md
├── api.md
├── project_structure.md
│
├── adr/
└── diagrams/
```

Purpose:

* System documentation
* Design decisions
* Deployment guides
* Architecture diagrams

---

## k8s/

Contains Kubernetes manifests required for deployment.

Typical files:

```text
k8s/
│
├── api-deployment.yaml
├── api-service.yaml
├── prometheus-deployment.yaml
├── prometheus-service.yaml
├── grafana-deployment.yaml
├── grafana-service.yaml
├── monitor-deployment.yaml
└── monitor-service.yaml
```

Responsibilities:

* Deploy application
* Configure services
* Configure monitoring
* Configure replica management

---

## logs/

Stores runtime application logs when logging is enabled.

Example:

```text
logs/
│
└── application.log
```

---

## mlruns/

Contains MLflow experiment tracking data.

Includes:

* Experiment metadata
* Parameters
* Metrics
* Model artifacts

This directory is automatically created by MLflow.

---

## monitoring/

Implements model and application monitoring.

Typical files:

```text
monitoring/
│
├── monitor.py
└── drift.py
```

Responsibilities:

* Calculate feature drift
* Export Prometheus metrics
* Monitor production data quality

---

## retraining/

Contains the automated retraining pipeline.

Typical structure:

```text
retraining/
│
├── config.py
├── feature_engineering.py
├── preprocessing.py
├── retrain.py
├── retraining_pipeline.py
├── save_artifacts.py
└── deploy.py
```

Responsibilities:

* Load new datasets
* Perform feature engineering
* Preprocess data
* Train candidate models
* Compare with production model
* Update production artifacts
* Trigger deployment

---

## tests/

Contains automated tests executed during Continuous Integration.

Example:

```text
tests/
│
├── test_api.py
├── test_model.py
├── test_metrics.py
└── test_retraining.py
```

Responsibilities:

* API validation
* Model loading tests
* Prediction tests
* Metrics verification
* Pipeline validation

---

## .github/

Contains GitHub-specific configuration.

Typical structure:

```text
.github/
│
└── workflows/
    ├── ci.yml
    └── cd.yml
```

Responsibilities:

* Continuous Integration
* Continuous Deployment
* Automated testing
* Docker image creation
* Deployment automation

---

# Project Organization Philosophy

The repository follows a modular design where each directory has a single responsibility.

* **Application Layer** handles prediction serving.
* **Training Layer** develops machine learning models.
* **Retraining Layer** automates model improvement.
* **Monitoring Layer** observes system health and feature drift.
* **Automation Layer** manages deployment decisions.
* **Infrastructure Layer** defines Docker and Kubernetes resources.
* **Documentation Layer** explains system design and operational procedures.

This separation reduces coupling between components, simplifies maintenance, and enables independent evolution of each subsystem.

---

# Repository Design Goals

The repository has been organized to achieve the following objectives:

* Maintain clear separation of concerns.
* Support reproducible machine learning experiments.
* Enable automated model retraining and deployment.
* Provide production-ready API serving.
* Facilitate containerized deployment using Docker.
* Support orchestration through Kubernetes.
* Enable monitoring and observability with Prometheus and Grafana.
* Encourage maintainable, scalable, and collaborative software development practices.

The resulting structure reflects common conventions used in modern production MLOps systems and provides a strong foundation for future extensions and cloud-native deployments.
