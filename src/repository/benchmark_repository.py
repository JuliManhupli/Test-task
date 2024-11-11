import json
from datetime import datetime
from typing import List

from src.entity.models import BenchmarkResult


def load_test_data() -> List[BenchmarkResult]:
    """
    Loads benchmarking test data from the 'test_database.json' file.

    Returns:
        List[BenchmarkResult]: A list of BenchmarkResult objects populated
        with the data from the JSON file.
    """
    with open("test_database.json", "r") as file:
        data = json.load(file)
        return [BenchmarkResult(**item) for item in data["benchmarking_results"]]


def get_all_results() -> List[BenchmarkResult]:
    """
    Retrieves all benchmarking results.

    Returns:
        List[BenchmarkResult]: A list of all BenchmarkResult objects.
    """
    return load_test_data()


def get_results_within_time_range(start_time: datetime, end_time: datetime) -> List[BenchmarkResult]:
    """
    Retrieves benchmarking results within a specified time range.

    Args:
        start_time (datetime): The start of the time range for filtering results.
        end_time (datetime): The end of the time range for filtering results.

    Returns:
        List[BenchmarkResult]: A list of BenchmarkResult objects that fall
        within the specified time range.
    """
    results = load_test_data()
    return [result for result in results if start_time <= result.timestamp <= end_time]
