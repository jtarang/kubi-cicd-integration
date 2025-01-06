# Stage 1: Build environment
FROM python:3.13-slim as builder

# Install system dependencies and Poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set up the working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock ./

# Install dependencies in a virtual environment
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Stage 2: Production environment
FROM python:3.13-slim

# Copy necessary files from the builder stage
COPY --from=builder /usr/local /usr/local

# Create a non-root user
RUN useradd -m appuser

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app/. .

# Change ownership to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
