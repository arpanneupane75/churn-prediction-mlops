import pandas as pd
import numpy as np

# =====================================================
# Load Data
# =====================================================

def load_data(train_path, test_path):

    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)

    df = pd.concat(
        [train_data, test_data],
        ignore_index=True
    )

    return df


# =====================================================
# Feature Engineering
# =====================================================

def feature_engineering(df):

    categorical_col = df.select_dtypes(
        include=["object"]
    ).columns.tolist()

    # -----------------------------------------
    # Encoding
    # -----------------------------------------

    subscription_map = {
        "Basic": 0,
        "Standard": 1,
        "Premium": 2
    }

    df["Subscription_Type_Num"] = (
        df["Subscription Type"]
        .map(subscription_map)
    )

    contract_map = {
        "Monthly": 0,
        "Quarterly": 1,
        "Annual": 2
    }

    df["Contract_Length_Num"] = (
        df["Contract Length"]
        .map(contract_map)
    )

    df["Gender"] = np.where(
        df["Gender"] == "Female",
        1,
        0
    )

    # -----------------------------------------
    # Drop original categorical columns
    # -----------------------------------------

    df_final = df.drop(columns=categorical_col)

    # -----------------------------------------
    # Feature Engineering
    # -----------------------------------------

    df_final["Avg_Spend_Per_Month"] = (
        df_final["Total Spend"] /
        (df_final["Tenure"] + 1)
    )

    df_final["Support_Calls_Per_Month"] = (
        df_final["Support Calls"] /
        (df_final["Tenure"] + 1)
    )

    df_final["Payment_Reliability"] = (
        1 /
        (df_final["Payment Delay"] + 1)
    )

    df_final["Engagement_Score"] = (

        df_final["Usage Frequency"] * 0.4 +

        (1 /
         (df_final["Support Calls"] + 1)) * 0.3 +

        (1 /
         (df_final["Payment Delay"] + 1)) * 0.3

    )

    # -----------------------------------------
    # Tenure Group
    # -----------------------------------------

    df_final["Tenure_Group"] = pd.cut(

        df_final["Tenure"],

        bins=[0, 6, 12, 24, 48, 100],

        labels=[
            "0-6",
            "6-12",
            "12-24",
            "24-48",
            "48+"
        ]
    )

    tenure_map = {

        "0-6": 0,
        "6-12": 1,
        "12-24": 2,
        "24-48": 3,
        "48+": 4

    }

    df_final["Tenure_Group_Num"] = (
        df_final["Tenure_Group"]
        .map(tenure_map)
    )

    # -----------------------------------------
    # Risk Features
    # -----------------------------------------

    df_final["High_Support_Risk"] = (
        df_final["Support Calls"] > 5
    ).astype(int)

    df_final["High_Payment_Risk"] = (
        df_final["Payment Delay"] > 10
    ).astype(int)

    df_final["Low_Usage_Risk"] = (

        df_final["Usage Frequency"]

        <

        df_final["Usage Frequency"].median()

    ).astype(int)

    # -----------------------------------------
    # Remove temporary feature
    # -----------------------------------------

    df_final = df_final.drop(
        columns=["Tenure_Group"]
    )

    return df_final