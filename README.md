# Benchmarking Results API

This is a FastAPI project that provides endpoints for retrieving average benchmarking performance statistics. It
includes functionality for fetching overall averages as well as averages within a specified time range.

## Features

- Retrieve average performance metrics for benchmarking results.
- Filter benchmarking results within a specified time range.
- Handle common error scenarios, including invalid date formats and no results found.

## Project Setup

### Requirements

- Python 3.8+
- Poetry (for dependency management and virtual environment handling)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JuliManhupli/Test-task
   cd Test-task
    ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
    ```
This will install all the required dependencies listed in the pyproject.toml file.

3. **Run the application**:

To run the FastAPI server, use the following command:
   ```bash
   uvicorn src.main:app --reload
   ```
This will start the application on http://127.0.0.1:8000.