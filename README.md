# MyRenderApiTest

A small FastAPI service that accepts a name, stores it in a relational database, and responds with a hello message.

## What this API does

- `POST /hello`
  - Input: `{ "name": "Ada" }`
  - Saves the name into the `name_entries` table.
  - Returns: `{ "id": 1, "message": "Hello Ada" }`
- `GET /health`
  - Returns service health.

## Tech stack

- FastAPI
- SQLAlchemy ORM
- Relational database:
  - PostgreSQL on Render (recommended in production)
  - SQLite locally (default fallback)

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) set `DATABASE_URL` from `.env.example`.
4. Run the API:

```bash
uvicorn main:app --reload
```

## Example request

```bash
curl -X POST http://127.0.0.1:8000/hello \
  -H "Content-Type: application/json" \
  -d '{"name":"Ada"}'
```

Example response:

```json
{
  "id": 1,
  "message": "Hello Ada"
}
```

## Deploying to Render

This repository includes `render.yaml`, so you can use Render Blueprint deploy:

1. Push this repo to GitHub.
2. In Render, choose **New +** → **Blueprint**.
3. Select your repository.
4. Render will create:
   - a web service (`my-render-api-test`)
   - a PostgreSQL database (`my-render-api-test-db`)
5. Deploy.

Render sets `DATABASE_URL` automatically from the database connection string.

## Project structure

- `main.py` - API endpoints and app setup
- `database.py` - DB engine/session/base setup
- `models.py` - SQLAlchemy table model
- `schemas.py` - request/response validation models
- `render.yaml` - Render deployment blueprint
