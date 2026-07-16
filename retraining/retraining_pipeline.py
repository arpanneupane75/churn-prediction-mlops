from retraining.config import (
    TRAIN_DATA,
    TEST_DATA
)

from retraining.feature_engineering import (
    load_data,
    feature_engineering
)

from retraining.preprocessing import (
    preprocess_data
)

from retraining.retrain import (
    train_models
)

from automation.compare_models import (
    compare_models
)

from retraining.save_artifacts import (
    save_artifacts
)

from retraining.deploy import (
    deploy_if_better
)


# =====================================================
# Main Retraining Pipeline
# =====================================================

def main():

    print("=" * 60)
    print("CUSTOMER CHURN RETRAINING PIPELINE")
    print("=" * 60)

    # -------------------------------------------------
    # Load Dataset
    # -------------------------------------------------

    print("\nLoading datasets...")

    df = load_data(
        TRAIN_DATA,
        TEST_DATA
    )

    print(f"Dataset Shape : {df.shape}")

    # -------------------------------------------------
    # Feature Engineering
    # -------------------------------------------------

    print("\nRunning feature engineering...")

    df_final = feature_engineering(df)

    print(f"Total Features : {len(df_final.columns)}")

    # -------------------------------------------------
    # Preprocessing
    # -------------------------------------------------

    print("\nRunning preprocessing...")

    processed = preprocess_data(df_final)

    print("Preprocessing completed.")

    # -------------------------------------------------
    # Model Training
    # -------------------------------------------------

    print("\nTraining models...")

    training_results = train_models(processed)

    # -------------------------------------------------
    # Compare with Production Model
    # -------------------------------------------------

    print("\nComparing with production model...")

    comparison = compare_models(

        new_model=training_results["best_model"],

        X_test=training_results["X_test_scaled"],

        y_test=training_results["y_test"]

    )

    # -------------------------------------------------
    # Deploy Only If Better
    # -------------------------------------------------

    if comparison["deploy"]:

        print("\nSaving new production artifacts...")

        # -------------------------------------------------
        # Best Model Metrics
        # -------------------------------------------------

        best_metrics = training_results["results_df"].loc[
            training_results["best_model_name"]
        ].to_dict()

        # -------------------------------------------------
        # Save Production Artifacts
        # -------------------------------------------------

        save_artifacts(

            model=training_results["best_model"],

            scaler=processed["scaler"],

            feature_names=processed["X_train"].columns.tolist(),

            X_train=processed["X_train"],

            model_name=training_results["best_model_name"],

            metrics=best_metrics

        )

        print("\nTriggering CI/CD Deployment...")

        deploy_if_better()

        deployment_status = "NEW MODEL DEPLOYED"

    else:

        deployment_status = "CURRENT MODEL RETAINED"

        print("\nCurrent production model performs better.")
        print("Skipping artifact replacement.")
        print(f"Reason: {comparison['reason']}")

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    print("\n" + "=" * 60)
    print("RETRAINING PIPELINE COMPLETED")
    print("=" * 60)

    print(f"Best Retrained Model : {training_results['best_model_name']}")
    print(f"Best F1 Score        : {training_results['best_f1']:.4f}")
    print(f"Deployment Status    : {deployment_status}")

    if comparison["reason"]:
        print(f"Reason               : {comparison['reason']}")

    print("=" * 60)


# =====================================================
# Entry Point
# =====================================================

if __name__ == "__main__":
    main()