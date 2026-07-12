import json
import joblib


# =====================================================
# Save Model, Scaler and Features
# =====================================================

def save_artifacts(
    model,
    scaler,
    feature_names,
    X_train
):

    # -----------------------------
    # Save model artifacts
    # -----------------------------

    joblib.dump(
        model,
        "churn_model.pkl"
    )

    joblib.dump(
        scaler,
        "scaler.pkl"
    )

    joblib.dump(
        feature_names,
        "feature_names.pkl"
    )

    print("Model artifacts saved successfully!")

    # -----------------------------
    # Create baseline statistics
    # -----------------------------

    baseline = {}

    numeric_columns = X_train.select_dtypes(
        include=["number"]
    ).columns

    for column in numeric_columns:

        baseline[column] = {

            "mean": float(
                X_train[column].mean()
            ),

            "std": float(
                X_train[column].std()
            ),

            "min": float(
                X_train[column].min()
            ),

            "max": float(
                X_train[column].max()
            )

        }

    with open(
        "baseline.json",
        "w"
    ) as f:

        json.dump(
            baseline,
            f,
            indent=4
        )

    print("Baseline saved successfully!")