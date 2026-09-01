# AGENTS.md

## Project overview

This repository contains a small FastAPI application for Mergington High School activities. The backend lives in [src/app.py](src/app.py), and the browser UI assets live under [src/static](src/static).

For product context and the exercise description, start with [README.md](README.md) and [src/README.md](src/README.md).

## Working conventions

- Keep the app simple and FastAPI-first; do not introduce persistent storage or a database layer unless the task explicitly requires it.
- The activity data is in-memory, so changes are ephemeral and reset when the server restarts.
- The frontend is served from the static files folder and the root route redirects to `/static/index.html`.
- Preserve the existing API contract for the activity endpoints unless the task explicitly changes it.

## Essential commands

Run the app from the repository root:

```bash
python -m uvicorn src.app:app --host 127.0.0.1 --port 8000 --reload
```

Run tests:

```bash
pytest
```

## Code-level expectations

- Prefer small, focused edits in [src/app.py](src/app.py) for backend changes.
- If the change affects the UI, keep the frontend and backend behavior aligned in [src/static](src/static).
- Validate behavior with the smallest relevant check: a targeted test when present, otherwise a local request against the running app.
- Do not break the core flow:
  - `GET /activities`
  - `POST /activities/{activity_name}/signup?email=student@mergington.edu`

## Notes for AI agents

- Use the repo root as the execution context unless a task specifically targets files under [src](src).
- If you add or change API behavior, update any relevant docs or examples to match the new contract.
- Keep the implementation consistent with the educational exercise: lightweight, readable, and easy to follow.
