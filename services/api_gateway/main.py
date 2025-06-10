import os

import httpx
from fastapi import FastAPI

AUTOMATION_URL = os.getenv("AUTOMATION_URL", "http://automation-svc:8000")

app = FastAPI(title="API Gateway")


@app.get("/")
async def root():
    return {"message": "API Gateway running"}


@app.post("/run")
async def run(model: str, prompt: str, tenant: str):
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{AUTOMATION_URL}/tasks",
            params={"model": model, "prompt": prompt, "tenant": tenant},
            timeout=60,
        )
    resp.raise_for_status()
    return resp.json()
