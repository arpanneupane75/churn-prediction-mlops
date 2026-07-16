import json
import os
from datetime import datetime

import joblib


# =====================================================
# Artifact Directory
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

ARTIFACT_DIR = os.path.join(
    BASE_DIR,
    "artifacts"
)


# =====================================================
# Save Production Artifacts
# =====================================================

def save_artifacts(
    model,
    scaler,
    feature_names,
    X_train,
    model_name,
    metrics
):

    # -------------------------------------------------
    # Create Artifact Directory
    # -------------------------------------------------

    os.makedirs(
        ARTIFACT_DIR,
        exist_ok=True
    )

    # -------------------------------------------------
    # File Paths
    # -------------------------------------------------

    model_path = os.path.join(
        ARTIFACT_DIR,
        "churn_model.pkl"
    )

    scaler_path = os.path.join(
        ARTIFACT_DIR,
        "scaler.pkl"
    )

    feature_path = os.path.join(
        ARTIFACT_DIR,
        "feature_names.pkl"
    )

    baseline_path = os.path.join(
        ARTIFACT_DIR,
        "baseline.json"
    )

    metadata_path = os.path.join(
        ARTIFACT_DIR,
        "model_metadata.json"
    )

    # -------------------------------------------------
    # Save Model Artifacts
    # -------------------------------------------------

    joblib.dump(
        model,
        model_path
    )

    joblib.dump(
        scaler,
        scaler_path
    )

    joblib.dump(
        feature_names,
        feature_path
    )

    # -------------------------------------------------
    # Create Baseline Statistics
    # -------------------------------------------------

    baseline = {}

    for column in X_train.columns:

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
        baseline_path,
        "w"
    ) as f:

        json.dump(
            baseline,
            f,
            indent=4
        )

    # -------------------------------------------------
    # Model Metadata
    # -------------------------------------------------

    metadata = {

        "model_name": model_name,

        "version": "1.0.0",

        "created_at": datetime.utcnow().isoformat(),

        "training_samples": len(X_train),

        "feature_count": len(feature_names),

        "features": feature_names,

        "metrics": {

            "accuracy": round(
                metrics["Accuracy"],
                4
            ),

            "precision": round(
                metrics["Precision"],
                4
            ),

            "recall": round(
                metrics["Recall"],
                4
            ),

            "f1_score": round(
                metrics["F1 Score"],
                4
            ),

            "roc_auc": round(
                metrics["ROC AUC"],
                4
            )

        }

    }

    with open(
        metadata_path,
        "w"
    ) as f:

        json.dump(
            metadata,
            f,
            indent=4
        )

    # -------------------------------------------------
    # Verify Saved Files
    # -------------------------------------------------

    print("\nProduction Artifacts")

    for file in [

        model_path,
        scaler_path,
        feature_path,
        baseline_path,
        metadata_path

    ]:

        if os.path.exists(file):

            print(f"✓ {os.path.basename(file)} saved")

        else:

            print(f"✗ Failed to save {os.path.basename(file)}")

    print("\nProduction artifacts created successfully.")