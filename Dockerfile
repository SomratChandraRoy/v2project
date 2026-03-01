# syntax=docker/dockerfile:1

FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=False

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY first_project/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY first_project/ .

# Create uploads directory
RUN mkdir -p /app/uploads

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose port
EXPOSE 8000

# Start gunicorn
CMD ["gunicorn", "first_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
