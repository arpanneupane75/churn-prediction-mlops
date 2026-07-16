# ADR-003: Docker Containerization Strategy

## Status

Accepted

---

## Context

The application consists of multiple independent services:

* FastAPI Prediction API
* Drift Monitoring Service
* Prometheus
* Grafana

Running these services directly on the operating system would introduce dependency conflicts and make deployment inconsistent across development environments.

The project also targets future deployment to Azure Kubernetes Service, which requires containerized workloads.

---

## Decision

Every application component is packaged as a Docker container.

The Prediction API and Drift Monitor each use dedicated Docker images built from lightweight Python base images.

Production artifacts, including the trained model, scaler, feature names, baseline statistics, and metadata, are bundled inside the API image to ensure reproducible deployments.

Prometheus and Grafana use their official container images.

---

## Rationale

Docker provides:

* Environment consistency
* Dependency isolation
* Reproducible deployments
* Simplified Kubernetes deployment
* Easy migration to cloud platforms

Bundling production artifacts within the API container guarantees that the exact model validated during training is the same model served during inference.

Using official Prometheus and Grafana images reduces maintenance effort while providing reliable monitoring components.

---

## Consequences

### Positive

* Portable deployments
* Consistent runtime environments
* Simplified Kubernetes integration
* Reduced dependency conflicts
* Faster application startup
* Easier CI/CD automation

### Negative

* Larger Docker image size because production artifacts are included
* Docker image must be rebuilt whenever the production model changes

---

## Technologies Used

* Docker
* Docker Desktop
* Python 3.13
* FastAPI
* Joblib
* Prometheus
* Grafana

---

## Future Considerations

When migrated to Azure Kubernetes Service, Docker images can be stored in Azure Container Registry or GitHub Container Registry without requiring application code changes.

The overall containerization strategy remains unchanged.
