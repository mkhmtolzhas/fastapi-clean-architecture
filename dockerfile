FROM python:3.13-slim

# Setting up pg_config
RUN apt-get update && apt-get install -y libpq-dev gcc

# Set the working directory
WORKDIR /app

# install poetry
RUN pip install --no-cache-dir poetry

# Copy the poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application code
COPY . .


# Expose the port the app runs on
ENV PORT=8000
EXPOSE $PORT


CMD alembic upgrade head && gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
