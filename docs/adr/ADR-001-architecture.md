# ADR-001: Modular MLOps Architecture

## Status

Accepted

---

## Context

The project aims to build an end-to-end MLOps pipeline for customer churn prediction rather than a standalone machine learning model. The system includes data preprocessing, feature engineering, model training, model evaluation, REST API deployment, monitoring, automated retraining, and CI/CD.

Initially, the project was implemented as a few large scripts. As the number of features increased, maintaining the code became increasingly difficult because changes in one module affected unrelated components.

The architecture also needed to support future migration from a local Kubernetes cluster to Azure Kubernetes Service (AKS) without requiring major code changes.

---

## Decision

The project is organized into independent modules, each responsible for a single stage of the machine learning lifecycle.

The repository is divided into components including:

* Data preprocessing
* Feature engineering
* Model training
* Artifact management
* REST API
* Monitoring
* Automated retraining
* Deployment automation
* Kubernetes manifests
* GitHub Actions workflows

Each module exposes reusable functions instead of embedding logic directly into scripts.

---

## Rationale

A modular architecture offers several advantages.

* Individual components can be tested independently.
* New models can be added without changing the deployment code.
* API development remains independent from training.
* Monitoring components can evolve without affecting inference.
* Retraining automation becomes significantly simpler.
* Future migration to Azure services requires minimal code modification.

This separation also follows common software engineering practices such as separation of concerns and single responsibility.

---

## Consequences

### Positive

* Improved maintainability
* Easier debugging
* Better code reuse
* Cleaner Git history
* Easier unit testing
* Scalable project structure
* Production-ready repository organization

### Negative

* More files to maintain
* Additional imports between modules
* Slightly higher initial development effort

---

## Technologies Affected

* Python
* FastAPI
* Scikit-learn
* MLflow
* Docker
* Kubernetes
* Prometheus
* Grafana
* GitHub Actions

---

## Future Considerations

The current modular architecture allows future integration with:

* Azure Machine Learning
* Azure Kubernetes Service
* Azure Container Registry
* Azure Monitor
* Azure DevOps

without restructuring the repository.
