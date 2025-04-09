# Use an official Python runtime
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Expose the port
EXPOSE 8000

# Run the app (adjust to your app's entry point)
CMD ["python3", "runner.py"]
