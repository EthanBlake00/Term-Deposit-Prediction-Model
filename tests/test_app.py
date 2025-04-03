import pytest

from app import app


@pytest.fixture
def client():
    """Creates a test client for the Flask app."""
    app.testing = True
    return app.test_client()


def test_home(client):
    """Test the home page loads successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"index.html" not in response.data  # Template should be rendered


def test_predict_success(client):
    """Test a successful prediction request."""
    data = {
        "age": "30",
        "job": "admin.",
        "marital": "married",
        "education": "basic.6y",
        "default": "no",
        "loan": "yes",
        "housing": "yes",
        "campaign": "2",
        "pdays": "5",
        "previous": "1",
        "poutcome": "success"
    }

    # Send the prediction request
    response = client.post("/predict", data=data)

    # Assert the status code and that the response contains the mock prediction result
    assert response.status_code == 200
    assert b"Yes" in response.data or b"No" in response.data


def test_predict_missing_data(client):
    """Test missing data scenario in the prediction route."""
    data = {
        "age": "30",
        "job": "admin."
        # Missing other required fields
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"Error: Missing data" in response.data


def test_predict_invalid_data(client):
    """Test invalid data input handling."""
    data = {
        "age": "invalid_age",  # Age should be an integer
        "job": "admin.",
        "marital": "married",
        "education": "basic.6y",
        "default": "no",
        "loan": "yes",
        "housing": "yes",
        "campaign": "2",
        "pdays": "5",
        "previous": "1",
        "poutcome": "success"
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"Error:" in response.data  # Error should be returned
