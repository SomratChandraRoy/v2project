# syntax=docker/dockerfile:1

FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=False

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY first_project/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY first_project/ .

# Create uploads directory
RUN mkdir -p /app/uploads

# Collect static files (use a build-time secret key)
RUN SECRET_KEY=build-only-key python manage.py collectstatic --no-input

# Copy entrypoint script
COPY first_project/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Create non-root user for security
RUN adduser --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Expose port
EXPOSE 8000

# Use entrypoint for migrations + gunicorn
ENTRYPOINT ["/app/entrypoint.sh"]
