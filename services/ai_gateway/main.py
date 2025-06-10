import os

import httpx
from fastapi import FastAPI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="AI Gateway")


@app.post("/ai/completions")
async def completions(model: str, prompt: str, tenant: str):
    if OPENAI_API_KEY:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                },
                timeout=30,
            )
        response.raise_for_status()
        data = response.json()
        result = data["choices"][0]["message"]["content"]
    else:
        # Fallback behavior when no API key provided
        result = prompt[::-1]
    return {"model": model, "prompt": prompt, "tenant": tenant, "result": result}
