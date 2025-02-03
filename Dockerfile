# Stage 1: Base Image
FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code
COPY ./src /app/src
COPY ./config /app/config

# Expose FastAPI default port
EXPOSE 8000

# Stage 2: Production Image
FROM base AS production

# Run the FastAPI app with Gunicorn and Uvicorn workers
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]