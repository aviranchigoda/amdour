FROM python:3.12-slim
WORKDIR /app
COPY ingest.py .
CMD ["python", "ingest.py", "--source", "quickbooks", "--tenant", "42"]
