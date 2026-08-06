"""API smoke tests for the ATHENA-X application."""

from fastapi.testclient import TestClient

from app.main import APP_DESCRIPTION, APP_TITLE, APP_VERSION, app

client = TestClient(app)


def test_root_endpoint_returns_application_metadata() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "name": APP_TITLE,
        "version": APP_VERSION,
        "description": APP_DESCRIPTION,
        "status": "running",
    }


def test_health_endpoint_returns_healthy_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
