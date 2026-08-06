# ATHENA-X

ATHENA-X is an institutional investment intelligence platform for fundamental analysis, valuation, risk assessment, portfolio optimization, and explainable investment decisions.

## Sprint 1: Core Bootstrap

This repository currently provides a production-ready FastAPI foundation with:

- Python 3.12 runtime support.
- FastAPI application metadata for ATHENA-X version `1.0.0`.
- Health and root API endpoints.
- Pydantic v2 and SQLAlchemy 2 dependencies.
- Docker and Docker Compose local runtime configuration.
- GitHub Actions CI for linting and tests.

## Project Structure

```text
app/
  api/
  core/
  database/
  engines/
  models/
  reports/
  services/
  utils/
  main.py
tests/
docs/
docker/
scripts/
data/
.github/workflows/
```

## API Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns application metadata and runtime status. |
| `GET` | `/health` | Returns service health for probes and monitoring. |

## Local Development

### Prerequisites

- Python 3.12
- Poetry

### Install dependencies

```bash
poetry install
```

### Run the API

```bash
poetry run uvicorn app.main:app --reload
```

The API is available at <http://127.0.0.1:8000> and interactive OpenAPI documentation is available at <http://127.0.0.1:8000/docs>.

### Run checks

```bash
poetry run ruff check .
poetry run pytest
```

## Docker

Build and run the API with Docker Compose:

```bash
docker compose up --build
```

The API container exposes port `8000` and includes a health check against `/health`.
