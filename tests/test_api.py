from fastapi.testclient import TestClient
from app import app


client = TestClient(app)



def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"]=="healthy"



def test_prediction():


    payload={

        "Age":35,
        "Tenure":24,
        "Usage_Frequency":20,
        "Support_Calls":2,
        "Payment_Delay":0,
        "Total_Spend":5000,
        "Last_Interaction":5,

        "Subscription_Type_Num":1,
        "Contract_Length_Num":2,

        "Avg_Spend_Per_Month":200,
        "Support_Calls_Per_Month":0.5,
        "Payment_Reliability":0.9,
        "Engagement_Score":0.8,

        "Tenure_Group_Num":2,

        "High_Support_Risk":0,
        "High_Payment_Risk":0,
        "Low_Usage_Risk":0
    }


    response=client.post(
        "/predict",
        json=payload
    )


    assert response.status_code==200


    result=response.json()


    assert "prediction" in result

    assert "probability" in result