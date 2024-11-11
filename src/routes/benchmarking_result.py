from datetime import datetime

from fastapi import APIRouter, HTTPException

from src.repository.benchmark_repository import get_all_results, get_results_within_time_range
from src.schemas.benchmarking_result import AverageStatistics
from src.services.results_service import calculate_averages

router = APIRouter(prefix='/results/average', tags=['benchmarking results'])


@router.get("/", response_model=AverageStatistics)
def get_average_performance() -> dict:
    """
    Retrieves the average benchmarking performance across all results.

    Returns:
        AverageStatistics: A dictionary containing the average performance statistics.

    Raises:
        HTTPException: If no benchmarking results are found, raises a 404 error.
    """
    results = get_all_results()
    if not results:
        raise HTTPException(status_code=404, detail="No benchmarking results found")
    return calculate_averages(results)


@router.get("/{start_time}/{end_time}", response_model=AverageStatistics)
def get_average_performance_in_time_range(start_time: str, end_time: str) -> dict:
    """
    Retrieves the average benchmarking performance within a specified time range.

    Args:
        start_time (str): The start time for filtering results (in ISO format).
        end_time (str): The end time for filtering results (in ISO format).

    Returns:
        AverageStatistics: A dictionary containing the average performance statistics
        for the results within the specified time range.

    Raises:
        HTTPException:
            - If the date format is invalid (not ISO format), raises a 400 error.
            - If start time is later than end time, raises a 400 error.
            - If no results are found in the specified time range, raises a 404 error.
    """
    try:
        start_time_dt = datetime.fromisoformat(start_time)
        end_time_dt = datetime.fromisoformat(end_time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Please use ISO format (YYYY-MM-DDTHH:MM:SS).")

    if start_time_dt > end_time_dt:
        raise HTTPException(status_code=400, detail="Start time must be earlier than or equal to end time.")

    results = get_results_within_time_range(start_time_dt, end_time_dt)
    if not results:
        raise HTTPException(status_code=404, detail="No benchmarking results found in the specified time range")
    return calculate_averages(results)
