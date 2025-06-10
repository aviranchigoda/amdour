from fastapi import FastAPI

app = FastAPI(title="API Gateway")


@app.get("/")
async def root():
    return {"message": "API Gateway running"}
