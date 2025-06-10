import os
from uuid import uuid4

import httpx
from fastapi import FastAPI, HTTPException

AI_GATEWAY_URL = os.getenv("AI_GATEWAY_URL", "http://ai-gateway:8000/ai/completions")

app = FastAPI(title="Automation Service")

# In-memory task store for demo purposes
TASKS: dict[str, dict] = {}


@app.post("/tasks")
async def create_task(model: str, prompt: str, tenant: str):
    task_id = str(uuid4())
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            AI_GATEWAY_URL,
            params={"model": model, "prompt": prompt, "tenant": tenant},
            timeout=60,
        )
    resp.raise_for_status()
    TASKS[task_id] = resp.json()
    return {"task_id": task_id}


@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    return TASKS[task_id]
