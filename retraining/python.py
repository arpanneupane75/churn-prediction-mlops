import pandas as pd

train = pd.read_csv("data/train_data.csv")
test = pd.read_csv("data/test_data.csv")

print("Train:", train.shape)
print("Test :", test.shape)

print("\nTrain Churn")
print(train["Churn"].value_counts(dropna=False))

print("\nTest Churn")
print(test["Churn"].value_counts(dropna=False))

print("\nTrain missing")
print(train["Churn"].isna().sum())

print("\nTest missing")
print(test["Churn"].isna().sum())