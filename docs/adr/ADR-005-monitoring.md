# ADR-005: Monitoring and Drift Detection

## Status

Accepted

---

## Context

Deploying a machine learning model without monitoring provides no visibility into application health or model behavior.

The project required monitoring for both operational metrics and machine learning performance.

Operational metrics include API usage and latency, while machine learning monitoring focuses on detecting feature drift between training data and production requests.

The monitoring solution also needed to integrate seamlessly with Kubernetes.

---

## Decision

Monitoring is implemented using Prometheus and Grafana.

A dedicated FastAPI-based Drift Monitoring Service exports Prometheus metrics describing feature drift.

Prometheus periodically scrapes metrics from:

* Prediction API
* Drift Monitoring Service

Grafana connects directly to Prometheus and visualizes the collected metrics through dashboards.

The monitoring system currently tracks:

### API Metrics

* Prediction Requests
* Prediction Errors
* Prediction Latency

### Model Monitoring Metrics

* Age Drift
* Tenure Drift
* Usage Frequency Drift
* Support Calls Drift
* Payment Delay Drift
* Total Spend Drift
* Last Interaction Drift

Baseline statistics used for drift detection are generated during model training and stored inside **baseline.json**.

---

## Rationale

Prometheus has become the industry standard for Kubernetes monitoring.

Its pull-based architecture integrates naturally with containerized workloads and provides efficient storage for time-series metrics.

Grafana provides interactive dashboards without requiring custom visualization code.

Separating drift monitoring into its own service keeps prediction latency low while allowing monitoring logic to evolve independently.

---

## Consequences

### Positive

* Centralized monitoring
* Real-time operational visibility
* Early detection of data drift
* Improved model reliability
* Better production observability
* Easy dashboard creation

### Negative

* Additional infrastructure components
* Increased resource usage
* Drift calculations require baseline maintenance

---

## Technologies Used

* Prometheus
* Grafana
* FastAPI
* prometheus_client
* Kubernetes

---

## Future Considerations

Future versions may include:

* Concept drift detection
* Automatic alerting
* Email or Teams notifications
* Azure Monitor integration
* Azure Managed Prometheus
* Azure Managed Grafana
