# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files (optional, if you use Django static files)
# RUN python manage.py collectstatic --noinput

# Expose port 8080 for GCP
EXPOSE 8080

# Start the Django app using Gunicorn
# ...existing code...
ENTRYPOINT ["sh", "-c", "python -m uvicorn chat_demo.asgi:application --host 0.0.0.0 --port ${PORT:-8080}"]
