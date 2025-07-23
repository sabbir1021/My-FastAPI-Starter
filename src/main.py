from fastapi import FastAPI
from src.routers import api_router

app = FastAPI(
    title="FastAPI Starter with Docker & CI/CD",
    version="1.0.0"
)

# Register all routers
app.include_router(api_router, prefix="/api/v1")
