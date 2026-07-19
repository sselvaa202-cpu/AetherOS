from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger
from app.api.auth import router as auth_router
from app.api.protected import router as protected_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

app.include_router(auth_router)
app.include_router(protected_router)

logger.info("AetherOS API Started")


@app.get("/")
def root():
    logger.info("Home endpoint accessed")

    return {
        "message": f"Welcome to {settings.app_name}"
    }


@app.get("/health")
def health():
    logger.info("Health endpoint accessed")

    return {
        "status": "Running",
        "version": settings.app_version,
        "debug": settings.debug
    }