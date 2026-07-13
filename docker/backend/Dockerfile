#
FROM python:3.13-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Print logs directly
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY backend/requirements/ ./requirements/

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements/development.txt

# Copy backend source
COPY backend/ .

# Expose Django port
EXPOSE 8000

# Start Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]