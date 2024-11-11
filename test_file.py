from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_average_performance():
    """Test the `get_average_performance` endpoint."""
    response = client.get("/results/average/")

    assert response.status_code == 200
    assert "average_token_count" in response.json()
    assert "average_time_to_first_token" in response.json()
    assert "average_time_per_output_token" in response.json()
    assert "average_total_generation_time" in response.json()


def test_get_average_performance_in_time_range_valid():
    """Test the `get_average_performance_in_time_range` endpoint with valid date range."""
    start_time = "2024-06-02T10:00:00"
    end_time = "2024-06-02T11:00:00"
    response = client.get(f"/results/average/{start_time}/{end_time}")

    assert response.status_code == 200
    assert "average_token_count" in response.json()
    assert "average_time_to_first_token" in response.json()
    assert "average_time_per_output_token" in response.json()
    assert "average_total_generation_time" in response.json()


def test_get_average_performance_in_time_range_invalid_format():
    """Test the `get_average_performance_in_time_range` endpoint with invalid date format."""
    start_time = "2024-11-01T00:00:00"
    end_time = "2024-11-02T23:59:59"
    response = client.get(f"/results/average/{start_time}/{end_time}x")

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid date format. Please use ISO format (YYYY-MM-DDTHH:MM:SS)."}


def test_get_average_performance_in_time_range_invalid_range():
    """Test the `get_average_performance_in_time_range` endpoint with invalid time range."""
    start_time = "2024-11-02T00:00:00"
    end_time = "2024-11-01T23:59:59"
    response = client.get(f"/results/average/{start_time}/{end_time}")

    assert response.status_code == 400
    assert response.json() == {"detail": "Start time must be earlier than or equal to end time."}


def test_get_average_performance_in_time_range_no_results():
    """Test the `get_average_performance_in_time_range` endpoint when no results are found in the time range."""
    start_time = "2025-11-01T00:00:00"
    end_time = "2025-11-02T23:59:59"
    response = client.get(f"/results/average/{start_time}/{end_time}")

    assert response.status_code == 404
    assert response.json() == {"detail": "No benchmarking results found in the specified time range"}
