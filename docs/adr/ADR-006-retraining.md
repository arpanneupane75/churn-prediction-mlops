# ADR-006: Automated Retraining and Continuous Deployment

## Status

Accepted

---

## Context

Machine learning models degrade over time as customer behavior changes.

Manual retraining is repetitive, error-prone, and increases the likelihood of deploying inferior models.

The project required an automated workflow capable of:

* Retraining models
* Comparing against the production model
* Updating production artifacts only when performance improves
* Triggering deployment automatically

The deployment pipeline also needed to remain compatible with future Azure Kubernetes Service deployment.

---

## Decision

An automated retraining pipeline was implemented.

The pipeline performs the following sequence:

1. Load training and testing datasets.
2. Perform feature engineering.
3. Execute preprocessing.
4. Train multiple machine learning models.
5. Select the highest-performing model.
6. Compare against the current production model.
7. Replace production artifacts only when the F1 Score improves beyond the configured threshold.
8. Commit updated artifacts automatically.
9. Push changes to the GitHub repository.
10. Trigger GitHub Actions Continuous Deployment.

Production artifacts include:

* churn_model.pkl
* scaler.pkl
* feature_names.pkl
* baseline.json
* metadata.json

GitHub Actions validates every update through the Continuous Integration workflow before the deployment workflow executes.

---

## Rationale

Automatically replacing production models without evaluation could decrease prediction quality.

By comparing every retrained model with the existing production model, the deployment pipeline guarantees that only demonstrably better models are promoted.

Automating Git commits and GitHub Actions removes manual deployment steps and improves reproducibility.

The workflow follows the same principles used in production MLOps platforms while remaining suitable for local Kubernetes deployment.

---

## Consequences

### Positive

* Automated retraining
* Objective model promotion
* Reproducible deployments
* Reduced manual intervention
* Version-controlled production artifacts
* CI validation before deployment
* Azure-ready deployment workflow

### Negative

* Longer retraining execution time
* Additional Git automation logic
* Model replacement depends on evaluation thresholds

---

## Technologies Used

* Python
* Scikit-learn
* MLflow
* Joblib
* Git
* GitHub Actions
* Docker
* Kubernetes

---

## Future Considerations

Future enhancements may include:

* Scheduled retraining
* Data versioning with DVC
* Azure Machine Learning Pipelines
* Azure Container Registry
* Azure Kubernetes Service deployment
* Automatic rollback after deployment failures
* Model Registry integration
