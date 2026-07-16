# ADR-004: Kubernetes Orchestration

## Status

Accepted

---

## Context

The Customer Churn Prediction system consists of multiple independent services that must communicate reliably while remaining isolated from one another.

The deployed application includes:

* FastAPI Prediction API
* Drift Monitoring Service
* Prometheus
* Grafana

Managing these services manually using Docker containers would become increasingly difficult as the application grows. Service discovery, restart policies, health monitoring, and scalability would also require additional manual configuration.

The project was designed locally using Docker Desktop Kubernetes while maintaining compatibility with Azure Kubernetes Service (AKS).

---

## Decision

Kubernetes was selected as the orchestration platform.

Each application component is deployed as an independent Kubernetes Deployment.

The project currently consists of four deployments:

* churn-api
* drift-monitor
* prometheus
* grafana

Each deployment runs a single replica because the project targets local development and demonstration.

Every deployment is exposed through its own Kubernetes Service, enabling internal communication between components.

The Prediction API additionally includes both readiness and liveness probes to allow Kubernetes to verify application health and automatically restart failed containers.

---

## Rationale

Kubernetes provides capabilities that are essential for production-ready MLOps systems.

These include:

* Automatic container restart
* Service discovery
* Health monitoring
* Declarative infrastructure
* Rolling updates
* Replica management
* Simplified scaling

Using Kubernetes also ensures that the application architecture closely resembles real-world production deployments used by cloud providers.

Deploying locally first allows the complete workflow to be validated before migrating to Azure Kubernetes Service.

---

## Consequences

### Positive

* Automatic recovery of failed containers
* Clean separation between application services
* Easier scaling by increasing replica counts
* Production-like deployment environment
* Cloud migration requires minimal configuration changes

### Negative

* Additional infrastructure complexity
* Higher memory consumption compared to running Docker containers directly
* Requires Kubernetes knowledge for troubleshooting

---

## Technologies Used

* Docker Desktop Kubernetes
* Kubernetes Deployments
* Kubernetes Services
* Readiness Probes
* Liveness Probes
* kubectl

---

## Future Considerations

The existing Kubernetes manifests are designed to be reusable for Azure Kubernetes Service.

Migration will primarily involve:

* Creating an AKS cluster
* Updating image registry references
* Applying the existing Kubernetes manifests

No significant application code changes are expected.
