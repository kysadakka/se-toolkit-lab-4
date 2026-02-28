"""End-to-end tests for the GET /interactions endpoint."""
import requests

def test_get_interactions_returns_200(API_BASE_URL, API_TOKEN):
    """Test that GET /interactions/ returns status code 200"""
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(f"{API_BASE_URL}/interactions/", headers=headers)
    assert response.status_code == 200

def test_get_interactions_response_is_a_list(API_BASE_URL, API_TOKEN):
    """Test that GET /interactions/ response body is a JSON array"""
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(f"{API_BASE_URL}/interactions/", headers=headers)
    data = response.json()
    assert isinstance(data, list)