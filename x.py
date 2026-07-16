import json

from retraining.feature_engineering import (
    load_data,
    feature_engineering
)

from retraining.preprocessing import (
    preprocess_data
)

from retraining.config import (
    TRAIN_DATA,
    TEST_DATA
)

# =====================================================
# Load and preprocess data
# =====================================================

df = load_data(
    TRAIN_DATA,
    TEST_DATA
)

df = feature_engineering(df)

processed = preprocess_data(df)

X_train = processed["X_train"]

# =====================================================
# Create baseline statistics
# =====================================================

baseline = {}

numeric_columns = X_train.select_dtypes(include=["number"]).columns

for col in numeric_columns:

    baseline[col] = {

        "mean": float(X_train[col].mean()),
        "std": float(X_train[col].std()),
        "min": float(X_train[col].min()),
        "max": float(X_train[col].max())

    }

# =====================================================
# Save baseline
# =====================================================

with open("artifacts/baseline.json", "w") as f:

    json.dump(
        baseline,
        f,
        indent=4
    )

print(f"baseline.json created successfully.")
print(f"Features saved: {len(baseline)}")