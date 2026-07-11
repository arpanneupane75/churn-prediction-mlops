from fastapi.testclient import TestClient
from app import app


client=TestClient(app)



def test_metrics():

    response=client.get("/metrics")


    assert response.status_code==200


    assert "prediction_requests_total" in response.text