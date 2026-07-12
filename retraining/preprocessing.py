import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif

from retraining.config import (
    RANDOM_STATE,
    TEST_SIZE
)


# =====================================================
# Train Test Split + Scaling
# =====================================================

def preprocess_data(df_final):

    # -----------------------------------------
    # Remove rows with missing target
    # -----------------------------------------

    missing_labels = df_final["Churn"].isna().sum()

    if missing_labels > 0:

        print(f"\nRemoving {missing_labels} rows with missing Churn labels...")

        df_final = (
            df_final
            .dropna(subset=["Churn"])
            .reset_index(drop=True)
        )

    # -----------------------------------------
    # Separate Features and Target
    # -----------------------------------------

    X = df_final.drop(
        columns=["CustomerID", "Churn"]
    )

    y = df_final["Churn"].astype(int)

    print(f"\nTraining samples : {len(X)}")
    print(f"Features          : {X.shape[1]}")
    print(f"Churn Distribution:\n{y.value_counts()}")

    # -----------------------------------------
    # Train Test Split
    # -----------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=TEST_SIZE,

        random_state=RANDOM_STATE,

        stratify=y

    )

    print(f"\nTraining Set : {len(X_train)}")
    print(f"Testing Set  : {len(X_test)}")

    # -----------------------------------------
    # Scaling
    # -----------------------------------------

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(
        X_train
    )

    X_test_scaled = scaler.transform(
        X_test
    )

    X_train_scaled_df = pd.DataFrame(
        X_train_scaled,
        columns=X_train.columns
    )

    X_test_scaled_df = pd.DataFrame(
        X_test_scaled,
        columns=X_test.columns
    )

    # -----------------------------------------
    # Feature Selection
    # (Same as Notebook)
    # -----------------------------------------

    selector = SelectKBest(
        score_func=f_classif,
        k=15
    )

    X_train_selected = selector.fit_transform(
        X_train_scaled,
        y_train
    )

    X_test_selected = selector.transform(
        X_test_scaled
    )

    selected_features = X_train.columns[
        selector.get_support()
    ].tolist()

    print("\nSelected Features:")

    for feature in selected_features:
        print(f" - {feature}")

    # -----------------------------------------
    # Return
    # -----------------------------------------

    return {

        "X_train": X_train,
        "X_test": X_test,

        "y_train": y_train,
        "y_test": y_test,

        "X_train_scaled": X_train_scaled,
        "X_test_scaled": X_test_scaled,

        "X_train_scaled_df": X_train_scaled_df,
        "X_test_scaled_df": X_test_scaled_df,

        "X_train_selected": X_train_selected,
        "X_test_selected": X_test_selected,

        "selected_features": selected_features,

        "scaler": scaler

    }