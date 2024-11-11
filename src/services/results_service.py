from typing import List

from src.entity.models import BenchmarkResult


def calculate_averages(results: List[BenchmarkResult]) -> dict:
    """
    Calculates the average performance statistics from a list of benchmarking results.

    Args:
        results (List[BenchmarkResult]): A list of BenchmarkResult objects containing the benchmarking results.

    Returns:
        dict: A dictionary containing the average performance statistics, with the following keys:
            - average_token_count (float): The average number of tokens in the generated text.
            - average_time_to_first_token (float): The average time (in milliseconds) taken to generate the first token.
            - average_time_per_output_token (float): The average time (in milliseconds) per output token.
            - average_total_generation_time (float): The average total time (in milliseconds) to generate the response.
    """
    total_token_count = sum(result.token_count for result in results)
    total_time_to_first_token = sum(result.time_to_first_token for result in results)
    total_time_per_output_token = sum(result.time_per_output_token for result in results)
    total_generation_time = sum(result.total_generation_time for result in results)

    count = len(results)
    return {
        "average_token_count": round(total_token_count / count, 2),
        "average_time_to_first_token": round(total_time_to_first_token / count, 2),
        "average_time_per_output_token": round(total_time_per_output_token / count, 2),
        "average_total_generation_time": round(total_generation_time / count, 2)
    }
