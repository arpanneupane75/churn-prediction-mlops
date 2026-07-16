# Deployment Guide

## Overview

The Customer Churn Prediction system follows a containerized deployment workflow designed to provide consistency across development, testing, and production environments. The application is packaged using Docker, orchestrated with Kubernetes, monitored using Prometheus and Grafana, and automated through GitHub Actions.

The deployment process separates model development from model serving, allowing production models to be updated independently while maintaining application stability.

---

# Deployment Architecture

The deployment workflow consists of the following stages:

```text
Developer
    │
    ▼
Git Repository
    │
    ▼
GitHub Actions (Continuous Integration)
    │
    ▼
Docker Image Build
    │
    ▼
Kubernetes Deployment
    │
    ▼
FastAPI Prediction Service
    │
    ▼
Prometheus Monitoring
    │
    ▼
Grafana Dashboards
```

---

# Local Development

Development begins on a local machine where models are trained, evaluated, and tested before deployment.

Typical development tasks include:

* Feature engineering
* Data preprocessing
* Model training
* Model evaluation
* API development
* Unit testing
* Retraining validation

Running the complete workflow locally allows rapid iteration before deploying changes.

---

# Docker Deployment

The prediction API is packaged into a Docker container.

Containerization provides several advantages:

* Consistent runtime environment
* Dependency isolation
* Simplified deployment
* Reproducible builds
* Easy migration between environments

The Docker image includes:

* FastAPI application
* Production model artifacts
* Python dependencies
* API server configuration

The monitoring service is packaged separately using an independent Docker image.

---

# Kubernetes Deployment

Kubernetes manages application deployment and lifecycle.

The project deploys the following components:

* Prediction API
* Drift monitoring service
* Prometheus
* Grafana

Kubernetes provides:

* Self-healing
* Replica management
* Rolling updates
* Service discovery
* Health monitoring
* Automatic restarts

Application availability is maintained through readiness and liveness probes.

---

# Continuous Integration

Continuous Integration is implemented using GitHub Actions.

Every push to the main branch automatically triggers:

* Repository checkout
* Python environment setup
* Dependency installation
* Automated testing
* Workflow validation

Only successful builds are eligible for deployment.

This ensures that production deployments are based on tested code.

---

# Continuous Deployment

The retraining pipeline automates deployment after model improvement.

The deployment process is:

1. Train multiple candidate models.
2. Evaluate model performance.
3. Compare against the production model.
4. Save new production artifacts if the candidate model is better.
5. Commit updated artifacts.
6. Push changes to GitHub.
7. Trigger GitHub Actions.
8. Build a new Docker image.
9. Deploy the updated application to Kubernetes.

If the retrained model does not outperform the production model, deployment is skipped.

This strategy prevents unnecessary production updates.

---

# Production Artifacts

Deployment relies on production-ready artifacts generated during retraining.

Artifacts include:

* Trained model
* Feature scaler
* Feature names
* Baseline statistics
* Model metadata

These artifacts are loaded by the FastAPI application during startup, ensuring that predictions use the latest approved production model.

---

# Health Checks

The deployed application exposes a health endpoint that allows Kubernetes to verify application availability.

Health checks are used for:

* Startup verification
* Readiness validation
* Liveness monitoring
* Automatic recovery

If a container becomes unhealthy, Kubernetes automatically restarts it.

---

# Scaling Strategy

The deployment architecture supports horizontal scaling.

Additional API replicas can be created without modifying the application code.

Benefits include:

* Increased throughput
* Improved availability
* Fault tolerance
* Load distribution across replicas

This enables the application to handle increasing prediction workloads.

---

# Monitoring Integration

Monitoring is integrated directly into the deployment.

Prometheus continuously collects:

* Prediction requests
* Request latency
* Prediction errors
* Feature drift metrics
* Application health metrics

Grafana visualizes these metrics through dashboards that provide operational visibility into the deployed system.

---

# Current Deployment Environment

The current implementation is deployed on a local Kubernetes cluster provided by Docker Desktop.

This environment is used for:

* Development
* Testing
* Demonstration
* End-to-end validation

The deployment configuration closely mirrors a production Kubernetes environment, making migration to a managed cloud Kubernetes service straightforward.

---

# Future Cloud Deployment

The architecture is designed to support deployment to Azure Kubernetes Service (AKS) with minimal changes.

Future cloud enhancements may include:

* Azure Container Registry (ACR) for image storage
* Azure Kubernetes Service (AKS) for orchestration
* Azure Monitor for centralized monitoring
* Azure Key Vault for secret management
* Managed ingress controllers
* Cloud-based persistent storage
* Autoscaling based on CPU or request load

Because the application is fully containerized and Kubernetes-native, the transition from a local cluster to AKS primarily involves infrastructure configuration rather than application changes.

---

# Deployment Benefits

The deployment strategy provides several operational advantages:

* Reproducible deployments through containerization
* Automated validation using Continuous Integration
* Controlled model updates through automated comparison
* High availability through Kubernetes orchestration
* Production monitoring using Prometheus and Grafana
* Clear separation between development, training, and serving
* Simplified migration to cloud-native environments

The resulting deployment pipeline demonstrates a production-oriented MLOps workflow that supports continuous improvement while maintaining application reliability and operational stability.
