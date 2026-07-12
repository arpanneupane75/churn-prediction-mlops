# import os
# import joblib

# from sklearn.metrics import (
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score,
#     roc_auc_score
# )


# MODEL_PATH = "artifacts/churn_model.pkl"


# def evaluate(model, X, y):

#     pred = model.predict(X)
#     prob = model.predict_proba(X)[:, 1]

#     return {

#         "Accuracy": accuracy_score(y, pred),

#         "Precision": precision_score(y, pred),

#         "Recall": recall_score(y, pred),

#         "F1": f1_score(y, pred),

#         "ROC_AUC": roc_auc_score(y, prob)

#     }


# def compare_models(
#         new_model,
#         X_test,
#         y_test,
#         new_model_name,
#         new_f1
# ):

#     print("=" * 60)
#     print("MODEL COMPARISON")
#     print("=" * 60)

#     # -----------------------------------------
#     # First deployment
#     # -----------------------------------------

#     if not os.path.exists(MODEL_PATH):

#         print("No production model found.")
#         print("Deploying first model.")

#         return True

#     # -----------------------------------------
#     # Load old model
#     # -----------------------------------------

#     old_model = joblib.load(MODEL_PATH)

#     old_metrics = evaluate(
#         old_model,
#         X_test,
#         y_test
#     )

#     new_metrics = evaluate(
#         new_model,
#         X_test,
#         y_test
#     )

#     print("\nProduction Model")

#     for k, v in old_metrics.items():
#         print(f"{k:12}: {v:.4f}")

#     print("\nRetrained Model")

#     for k, v in new_metrics.items():
#         print(f"{k:12}: {v:.4f}")

#     print("\nDecision")

#     improvement = new_metrics["F1"] - old_metrics["F1"]

#     print(f"Old F1 : {old_metrics['F1']:.4f}")
#     print(f"New F1 : {new_metrics['F1']:.4f}")
#     print(f"Gain   : {improvement:.4f}")

#     if improvement > 0.005:

#         print("\nRetrained model is better.")
#         print("Replacing production model.")

#         return True

#     print("\nImprovement is insignificant.")
#     print("Keeping current production model.")

#     return False

import os
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


MODEL_PATH = "artifacts/churn_model.pkl"

# Minimum improvement required before replacing production model
MIN_F1_IMPROVEMENT = 0.005


# =====================================================
# Evaluate Model
# =====================================================

def evaluate(model, X, y):

    pred = model.predict(X)
    prob = model.predict_proba(X)[:, 1]

    return {

        "Accuracy": accuracy_score(y, pred),

        "Precision": precision_score(y, pred),

        "Recall": recall_score(y, pred),

        "F1": f1_score(y, pred),

        "ROC_AUC": roc_auc_score(y, prob)

    }


# =====================================================
# Compare Production vs Retrained Model
# =====================================================

def compare_models(
        new_model,
        X_test,
        y_test,
        new_model_name,
        new_f1
):

    print("=" * 60)
    print("MODEL COMPARISON")
    print("=" * 60)

    # -------------------------------------------------
    # First Deployment
    # -------------------------------------------------

    if not os.path.exists(MODEL_PATH):

        print("No production model found.")
        print("Deploying first model.")

        return {

            "deploy": True,
            "reason": "First deployment",

            "old_metrics": None,

            "new_metrics": evaluate(
                new_model,
                X_test,
                y_test
            )

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

    new_metrics = evaluate(
        new_model,
        X_test,
        y_test
    )

    print("\nProduction Model")

    for k, v in old_metrics.items():
        print(f"{k:12}: {v:.4f}")

    print("\nRetrained Model")

    for k, v in new_metrics.items():
        print(f"{k:12}: {v:.4f}")

    improvement = new_metrics["F1"] - old_metrics["F1"]

    print("\nDecision")
    print(f"Old F1 : {old_metrics['F1']:.4f}")
    print(f"New F1 : {new_metrics['F1']:.4f}")
    print(f"Gain   : {improvement:.4f}")

    if improvement >= MIN_F1_IMPROVEMENT:

        print("\nRetrained model is better.")
        print("Replacing production model.")

        return {

            "deploy": True,

            "reason": f"F1 improved by {improvement:.4f}",

            "old_metrics": old_metrics,

            "new_metrics": new_metrics

        }

    print("\nImprovement is insignificant.")
    print("Keeping current production model.")

    return {

        "deploy": False,

        "reason": f"F1 improvement ({improvement:.4f}) below threshold",

        "old_metrics": old_metrics,

        "new_metrics": new_metrics

    }