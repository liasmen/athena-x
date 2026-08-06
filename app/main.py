"""Application entrypoint for the ATHENA-X API."""

from fastapi import FastAPI

APP_TITLE = "ATHENA-X"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Institutional Investment Intelligence Platform"

app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)


@app.get("/", tags=["Root"])
def read_root() -> dict[str, str]:
    """Return basic application information."""
    return {
        "name": APP_TITLE,
        "version": APP_VERSION,
        "description": APP_DESCRIPTION,
        "status": "running",
    }


@app.get("/health", tags=["Health"])
def read_health() -> dict[str, str]:
    """Return service health status for orchestration probes."""
    return {"status": "healthy"}
