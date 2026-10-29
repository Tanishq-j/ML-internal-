# Lightweight Python Docker Image
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy application source code
COPY hello.py .

# Run the hello.py application
ENTRYPOINT ["python", "hello.py"]
