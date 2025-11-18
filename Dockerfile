FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy *entire* project folder (not just src)
COPY . .

# Ensure Python can import from /app
ENV PYTHONPATH="/app"

# Create required folders for pipeline / logs
RUN mkdir -p /data/input /data/output /data/logs

# Run Flask API using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "src.app:app"]
