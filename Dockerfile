# Written by Amir Hossin Moulodi

# 1. Base Image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# 3. Install Poetry
RUN pip install poetry

# 4. Copy dependency files and install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev && rm -rf $POETRY_CACHE_DIR

# 5. Copy the application code
COPY ./src /app/src

# 6. Command to run the app
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]