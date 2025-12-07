# ===========================
# 1. Use official Python base image
# ===========================
FROM python:3.11-slim

# ===========================
# 2. Environment variables
# ===========================
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ===========================
# 3. Working directory
# ===========================
WORKDIR /app

# ===========================
# 4. Install system dependencies
# ===========================
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# ===========================
# 5. Copy dependency list and install
# ===========================
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ===========================
# 6. Copy project files
# ===========================
COPY . .

# ===========================
# 7. Expose port
# ===========================
EXPOSE 8000

# ===========================
# 8. Run Gunicorn WSGI server
# ===========================
CMD ["gunicorn", "storemanagement.wsgi:application", "--bind", "0.0.0.0:8000"]
