import os
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# =====================================================
# Configuration
# =====================================================

MODEL_PATH = "artifacts/churn_model.pkl"

# Minimum F1 improvement required to replace production model
MIN_F1_IMPROVEMENT = 0.005


# =====================================================
# Evaluate Model
# =====================================================

def evaluate(model, X, y):

    predictions = model.predict(X)
    probabilities = model.predict_proba(X)[:, 1]

    return {

        "Accuracy": accuracy_score(y, predictions),

        "Precision": precision_score(y, predictions),

        "Recall": recall_score(y, predictions),

        "F1": f1_score(y, predictions),

        "ROC_AUC": roc_auc_score(y, probabilities)

    }


# =====================================================
# Compare Production vs Retrained Model
# =====================================================

def compare_models(
    new_model,
    X_test,
    y_test
):

    print("=" * 60)
    print("MODEL COMPARISON")
    print("=" * 60)

    # -------------------------------------------------
    # Evaluate Retrained Model
    # -------------------------------------------------

    new_metrics = evaluate(
        new_model,
        X_test,
        y_test
    )

    # -------------------------------------------------
    # First Deployment
    # -------------------------------------------------

    if not os.path.exists(MODEL_PATH):

        print("\nNo production model found.")
        print("Deploying first model.")

        return {

            "deploy": True,

            "reason": "First deployment",

            "old_metrics": None,

            "new_metrics": new_metrics

        }

    # -------------------------------------------------
    # Load Production Model
    # -------------------------------------------------

    old_model = joblib.load(MODEL_PATH)

    old_metrics = evaluate(
        old_model,
        X_test,
        y_test
    )

    # -------------------------------------------------
    # Display Metrics
    # -------------------------------------------------

    print("\nProduction Model")

    for metric, value in old_metrics.items():
        print(f"{metric:12}: {value:.4f}")

    print("\nRetrained Model")

    for metric, value in new_metrics.items():
        print(f"{metric:12}: {value:.4f}")

    # -------------------------------------------------
    # Compare Performance
    # -------------------------------------------------

    improvement = new_metrics["F1"] - old_metrics["F1"]

    print("\nDecision")
    print(f"Old F1 : {old_metrics['F1']:.4f}")
    print(f"New F1 : {new_metrics['F1']:.4f}")
    print(f"Gain   : {improvement:.4f}")

    # -------------------------------------------------
    # Deploy If Better
    # -------------------------------------------------

    if improvement >= MIN_F1_IMPROVEMENT:

        print("\nRetrained model is better.")
        print("Replacing production model.")

        return {

            "deploy": True,

            "reason": f"F1 improved by {improvement:.4f}",

            "old_metrics": old_metrics,

            "new_metrics": new_metrics

        }

    # -------------------------------------------------
    # Keep Existing Production Model
    # -------------------------------------------------

    print("\nImprovement is insignificant.")
    print("Keeping current production model.")

    return {

        "deploy": False,

        "reason": f"F1 improvement ({improvement:.4f}) below threshold",

        "old_metrics": old_metrics,

        "new_metrics": new_metrics

    }