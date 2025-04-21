# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copy only the files needed to install dependencies
COPY /pyproject.toml /app/
COPY /poetry.lock /app 

# Install dependencies
WORKDIR /app
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy  source code
COPY  . /app

# Expose the default FastAPI port
EXPOSE 8000

# Run the app using uvicorn
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]
