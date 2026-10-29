# MLOps UAT Environment & Pipeline Project

This repository contains a lightweight single-file Python application, containerization setup, CI/CD Jenkins configuration, test automation using pytest, and model monitoring with Evidently AI.

## Project Structure
```
MLOps/
├── .gitignore               # Git ignore patterns
├── Dockerfile               # Lightweight Python Alpine Docker image
├── Jenkinsfile              # Jenkins Declarative CI/CD pipeline definition
├── README.md                # Project documentation and setup guide
├── evidently_metrics.json   # Output metrics from Evidently AI
├── evidently_monitor.py     # Data and model drift monitoring script
├── hello.py                 # Core single-file application & scoring service
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Project dependencies
└── tests/
    └── test_hello.py        # Automated test suite (pytest)
```

## Prerequisites & Installed Tools
- **Python**: 3.11.x
- **Docker**: Docker Desktop / Engine 29.8.x
- **Jenkins**: Jenkins LTS
- **Pytest**: Automated testing framework
- **Evidently AI**: Data drift and model health monitoring

## Quick Start Guide

### 1. Run the Python Application
```bash
python hello.py "DevOps Engineer"
```

### 2. Execute Pytest Suite
```bash
pytest -v tests/test_hello.py
```

### 3. Build & Run Docker Container
```bash
# Pull lightweight Python base image
docker pull python:3.11-alpine

# Build Docker image
docker build -t hello-mlops-app:latest .

# Run container
docker run --rm hello-mlops-app:latest "Docker UAT"
```

### 4. Run Evidently AI Drift Monitoring
```bash
python evidently_monitor.py
```
This generates:
- `evidently_report.html`: Interactive visual report.
- `evidently_metrics.json`: Machine-readable drift and data quality metrics.

### 5. Jenkins CI/CD Pipeline
- Configure a Jenkins pipeline job pointing to this repository (`https://github.com/Tanishq-j/ML-internal-.git`).
- The pipeline executes checkout, testing, container build, and Evidently monitoring stages.
