import joblib



def test_model_files():


    model=joblib.load(
        "artifacts/churn_model.pkl"
    )


    scaler=joblib.load(
        "artifacts/scaler.pkl"
    )


    features=joblib.load(
        "artifacts/feature_names.pkl"
    )


    assert model is not None

    assert scaler is not None

    assert len(features)>0