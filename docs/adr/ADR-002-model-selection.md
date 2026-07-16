# ADR-002: Multi-Model Training and Automatic Model Selection

## Status

Accepted

---

## Context

Customer churn prediction is a binary classification problem. Selecting the best-performing algorithm before deployment is essential because different models perform differently depending on the dataset.

Deploying the first working model without comparison would reduce confidence in production performance.

The retraining pipeline also requires an objective method for determining whether a newly trained model should replace the production model.

---

## Decision

During every training cycle, the pipeline trains four machine learning algorithms:

* Logistic Regression
* Random Forest
* Gradient Boosting
* XGBoost

Each model is evaluated using the same train/test split.

Evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

The model with the highest F1 Score is selected as the candidate production model.

During retraining, the candidate model is compared against the existing production model.

The production model is replaced only if the F1 Score improves beyond the configured threshold.

---

## Rationale

The dataset is moderately imbalanced, making F1 Score a better deployment metric than Accuracy.

Training multiple models provides:

* Objective comparison
* Reduced model bias
* Better reproducibility
* Improved deployment confidence

Keeping the previous production model unless measurable improvement exists prevents unnecessary model replacement and production instability.

---

## Consequences

### Positive

* Consistent evaluation
* Automated best model selection
* Stable production deployments
* Reproducible experiments
* Better overall prediction quality

### Negative

* Increased training time
* Higher computational requirements
* Additional evaluation logic

---

## Technologies Used

* Scikit-learn
* XGBoost
* MLflow
* Joblib

---

## Future Considerations

Future versions may evaluate additional algorithms such as:

* LightGBM
* CatBoost
* Neural Networks

without changing the overall training workflow.
