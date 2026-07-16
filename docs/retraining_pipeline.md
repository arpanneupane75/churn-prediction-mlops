# Automated Retraining Pipeline

## Overview

The retraining pipeline is responsible for continuously improving the production machine learning model. Instead of replacing the deployed model after every training run, the pipeline evaluates newly trained models against the current production model and only deploys the new model if it demonstrates a meaningful performance improvement.

This approach minimizes unnecessary deployments while ensuring that production models improve over time as new training data becomes available.

---

# Pipeline Objectives

The retraining pipeline is designed to achieve the following objectives:

* Automatically train candidate machine learning models.
* Evaluate multiple algorithms using common classification metrics.
* Compare the best retrained model with the current production model.
* Update production artifacts only when the new model performs better.
* Preserve reproducibility by saving all required inference artifacts.
* Trigger the Continuous Integration and Continuous Deployment workflow after a successful model update.

---

# Pipeline Workflow

The retraining process follows the workflow shown below.

```text
Training Dataset
        │
        ▼
Load Dataset
        │
        ▼
Feature Engineering
        │
        ▼
Data Preprocessing
        │
        ▼
Train Multiple Models
        │
        ▼
Model Evaluation
        │
        ▼
Select Best Model
        │
        ▼
Compare With Production Model
        │
        ▼
Is New Model Better?
     │           │
    Yes          No
     │           │
     ▼           ▼
Save Artifacts   Keep Existing Model
     │
     ▼
Commit Changes
     │
     ▼
Push to GitHub
     │
     ▼
GitHub Actions
```

---

# Pipeline Stages

## 1. Dataset Loading

The pipeline begins by loading the available training and testing datasets.

Responsibilities include:

* Reading customer churn datasets.
* Validating dataset availability.
* Combining datasets when required.
* Preparing data for feature engineering.

---

## 2. Feature Engineering

Additional business-oriented features are generated from the raw customer information.

Examples include:

* Average Spend Per Month
* Payment Reliability
* Engagement Score
* Support Calls Per Month
* High Payment Risk
* High Support Risk
* Low Usage Risk

Feature engineering improves model performance by capturing relationships that are not directly available in the original dataset.

---

## 3. Data Preprocessing

The preprocessing stage prepares the engineered dataset for machine learning.

Operations include:

* Removing invalid records.
* Handling missing values.
* Encoding categorical variables.
* Scaling numerical features.
* Splitting data into training and testing sets.

The fitted scaler is saved as a production artifact for use during inference.

---

## 4. Model Training

Multiple machine learning algorithms are trained using the prepared dataset.

Current models include:

* Logistic Regression
* Random Forest
* Gradient Boosting
* XGBoost

Training multiple models enables objective comparison rather than relying on a single algorithm.

---

## 5. Model Evaluation

Each trained model is evaluated using a common set of performance metrics.

Metrics include:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

The model achieving the highest F1 Score is selected as the candidate production model.

---

## 6. Production Model Comparison

The candidate model is compared against the currently deployed production model.

The comparison process:

1. Loads the production model.
2. Evaluates both models on the same testing dataset.
3. Calculates evaluation metrics.
4. Computes the performance improvement.
5. Determines whether deployment should occur.

If no production model exists, the candidate model becomes the initial production model.

---

## 7. Artifact Generation

When deployment is approved, the pipeline generates production-ready artifacts.

Artifacts include:

* Trained model
* Feature scaler
* Feature names
* Baseline statistics
* Model metadata

These artifacts are stored in the `artifacts/` directory and are later consumed by the FastAPI inference service.

---

## 8. Automated Deployment Trigger

After successfully updating production artifacts, the deployment automation performs the following actions:

* Stages modified files.
* Creates a Git commit.
* Pushes changes to the GitHub repository.

The push automatically triggers the GitHub Actions workflow, initiating Continuous Integration and the deployment pipeline.

---

# Deployment Decision Logic

The retraining pipeline follows a conservative deployment strategy.

The production model is replaced only when:

* A candidate model successfully completes training.
* Performance evaluation is successful.
* The candidate model demonstrates measurable improvement over the production model.
* Production artifacts are generated successfully.
* Deployment automation completes without errors.

If these conditions are not satisfied, the current production model remains unchanged.

This prevents unnecessary deployments caused by statistically insignificant improvements.

---

# Production Artifacts

The retraining pipeline produces the following artifacts.

| Artifact            | Purpose                                  |
| ------------------- | ---------------------------------------- |
| `churn_model.pkl`   | Production machine learning model        |
| `scaler.pkl`        | Feature scaling during inference         |
| `feature_names.pkl` | Maintains feature ordering               |
| `baseline.json`     | Baseline statistics for drift monitoring |
| `metadata.json`     | Model information and evaluation metrics |

These artifacts allow the deployed application to perform consistent predictions without requiring retraining.

---

# Error Handling

The retraining pipeline includes safeguards to improve reliability.

Examples include:

* Missing dataset detection.
* Invalid artifact handling.
* Production model existence checks.
* Deployment failure detection.
* Git operation validation.
* Artifact generation verification.

Failures during deployment do not overwrite the existing production model, preserving system stability.

---

# Benefits of the Retraining Pipeline

The automated retraining pipeline provides several operational advantages.

* Eliminates manual model replacement.
* Ensures reproducible model deployment.
* Maintains production stability through controlled deployment decisions.
* Supports continuous model improvement.
* Preserves production artifacts for inference.
* Integrates naturally with Continuous Integration and Continuous Deployment workflows.

This design reflects common production MLOps practices, where model updates are governed by objective performance evaluation rather than manual intervention.
