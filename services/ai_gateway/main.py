from fastapi import FastAPI

app = FastAPI(title="AI Gateway")


@app.post("/ai/completions")
async def completions(model: str, prompt: str, tenant: str):
    return {"model": model, "prompt": prompt, "tenant": tenant, "result": "..."}
