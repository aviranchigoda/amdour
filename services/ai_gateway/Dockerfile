FROM python:3.12-slim
WORKDIR /app
RUN pip install fastapi uvicorn httpx sqlmodel redis
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
