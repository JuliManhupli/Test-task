from pydantic import BaseModel


class AverageStatistics(BaseModel):
    average_token_count: float
    average_time_to_first_token: float
    average_time_per_output_token: float
    average_total_generation_time: float
