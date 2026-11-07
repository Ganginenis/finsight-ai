from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "application": "FinSight AI",
        "message": "Welcome to FinSight AI",
        "version": "0.1.0",
    }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["application"] == "FinSight AI"


def test_openapi_documentation():
    response = client.get("/openapi.json")

    assert response.status_code == 200

    schema = response.json()

    assert "/" in schema["paths"]
    assert "/health" in schema["paths"]


def test_unknown_endpoint_returns_404():
    response = client.get("/unknown-endpoint")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }


def test_versioned_api_root():
    response = client.get("/api/v1/")

    assert response.status_code == 200

    assert response.json() == {
        "api_version": "v1",
        "message": "FinSight AI API is operational",
    }
