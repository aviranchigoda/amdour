from fastapi import FastAPI

app = FastAPI(title="Auth Service")


@app.post("/auth/signup")
async def signup():
    return {"token": "fake-jwt"}


@app.get("/tenants/{tenant_id}/users")
async def list_users(tenant_id: int):
    return [{"id": 1, "name": "Admin", "tenant_id": tenant_id}]
