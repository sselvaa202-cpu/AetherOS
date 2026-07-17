from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

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