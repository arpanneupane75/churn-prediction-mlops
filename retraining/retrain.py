import pandas as pd
import mlflow
import mlflow.sklearn
import mlflow.xgboost

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from retraining.config import RANDOM_STATE


# =====================================================
# Train Models
# =====================================================

def train_models(preprocessed_data):

    X_train_scaled = preprocessed_data["X_train_scaled"]
    X_test_scaled = preprocessed_data["X_test_scaled"]

    y_train = preprocessed_data["y_train"]
    y_test = preprocessed_data["y_test"]

    # ----------------------------------------------------
    # MLflow Experiment
    # ----------------------------------------------------

    mlflow.set_experiment("Customer Churn")

    # ----------------------------------------------------
    # Models
    # ----------------------------------------------------

    models = {

        "Logistic Regression": LogisticRegression(
            random_state=RANDOM_STATE,
            max_iter=1000
        ),

        "Random Forest": RandomForestClassifier(
            random_state=RANDOM_STATE,
            n_estimators=100
        ),

        "Gradient Boosting": GradientBoostingClassifier(
            random_state=RANDOM_STATE
        ),

        "XGBoost": XGBClassifier(
            random_state=RANDOM_STATE,
            eval_metric="logloss"
        )

    }

    results = {}

    best_model = None
    best_model_name = None
    best_f1 = -1

    # ----------------------------------------------------
    # Training Loop
    # ----------------------------------------------------

    for name, model in models.items():

        with mlflow.start_run(run_name=name):

            # ----------------------------
            # Train
            # ----------------------------

            model.fit(
                X_train_scaled,
                y_train
            )

            # ----------------------------
            # Predict
            # ----------------------------

            y_pred = model.predict(
                X_test_scaled
            )

            y_prob = model.predict_proba(
                X_test_scaled
            )[:, 1]

            # ----------------------------
            # Metrics
            # ----------------------------

            accuracy = accuracy_score(
                y_test,
                y_pred
            )

            precision = precision_score(
                y_test,
                y_pred
            )

            recall = recall_score(
                y_test,
                y_pred
            )

            f1 = f1_score(
                y_test,
                y_pred
            )

            roc_auc = roc_auc_score(
                y_test,
                y_prob
            )

            # ----------------------------
            # Store Results
            # ----------------------------

            results[name] = {

                "Accuracy": accuracy,
                "Precision": precision,
                "Recall": recall,
                "F1 Score": f1,
                "ROC AUC": roc_auc

            }

            # ----------------------------
            # Log Parameters
            # ----------------------------

            mlflow.log_param(
                "model_name",
                name
            )

            mlflow.log_param(
                "random_state",
                RANDOM_STATE
            )

            if name == "Logistic Regression":

                mlflow.log_param(
                    "max_iter",
                    model.max_iter
                )

            elif name == "Random Forest":

                mlflow.log_param(
                    "n_estimators",
                    model.n_estimators
                )

            elif name == "Gradient Boosting":

                mlflow.log_param(
                    "n_estimators",
                    model.n_estimators
                )

                mlflow.log_param(
                    "learning_rate",
                    model.learning_rate
                )

            elif name == "XGBoost":

                params = model.get_params()

                mlflow.log_param(
                    "n_estimators",
                    params["n_estimators"]
                )

                mlflow.log_param(
                    "learning_rate",
                    params["learning_rate"]
                )

                mlflow.log_param(
                    "max_depth",
                    params["max_depth"]
                )

                mlflow.log_param(
                    "eval_metric",
                    params["eval_metric"]
                )

            # ----------------------------
            # Log Metrics
            # ----------------------------

            mlflow.log_metric(
                "Accuracy",
                accuracy
            )

            mlflow.log_metric(
                "Precision",
                precision
            )

            mlflow.log_metric(
                "Recall",
                recall
            )

            mlflow.log_metric(
                "F1 Score",
                f1
            )

            mlflow.log_metric(
                "ROC AUC",
                roc_auc
            )

            # ----------------------------
            # Log Model
            # ----------------------------

            if name == "XGBoost":

                mlflow.xgboost.log_model(
                    xgb_model=model,
                    name="model"
                )

            else:

                mlflow.sklearn.log_model(
                    sk_model=model,
                    name="model"
                )

            # ----------------------------
            # Best Model
            # ----------------------------

            if f1 > best_f1:

                best_f1 = f1
                best_model = model
                best_model_name = name

    # ----------------------------------------------------
    # Results Table
    # ----------------------------------------------------

    results_df = pd.DataFrame(results).T

    print("\n==============================")
    print("MODEL COMPARISON")
    print("==============================")
    print(results_df.round(4))

    print("\nBest Model :", best_model_name)
    print("Best F1    :", round(best_f1, 4))

    return {

        "best_model": best_model,

        "best_model_name": best_model_name,

        "best_f1": best_f1,

        "results_df": results_df,

        "models": models,

        "X_test_scaled": X_test_scaled,

        "y_test": y_test

    }