import joblib



def test_model_files():


    model=joblib.load(
        "churn_model.pkl"
    )


    scaler=joblib.load(
        "scaler.pkl"
    )


    features=joblib.load(
        "feature_names.pkl"
    )


    assert model is not None

    assert scaler is not None

    assert len(features)>0