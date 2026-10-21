# SprintBoard — Agile + DevOps Mini Project

A small Kanban-style task tracker used to demonstrate an **end-to-end DevOps pipeline**:

`Jira (Plan) → GitHub (Code) → GitHub Actions (Build/Test) → Docker (Package) → Deploy → Verify`

## Tech stack
| Stage | Tool |
|---|---|
| Planning / tracking | Jira (Scrum board) |
| Source control | Git + GitHub |
| CI | GitHub Actions |
| Packaging | Docker (+ docker-compose) |
| App | Python 3.12, Flask, Gunicorn |
| Testing / lint | pytest, flake8 |

## Project layout
```
sprintboard/
├── app/                    Flask application (REST API + board UI)
├── tests/                  pytest unit tests
├── docs/
│   ├── SPRINT_PLAN.md      Agile artefacts: backlog, user stories, sprints, Jira issues
│   └── EXPERIMENT_REPORT.md  Lab report (Experiment 10) filled for this project
├── .github/workflows/ci.yml  CI pipeline
├── Dockerfile
├── docker-compose.yml
└── wsgi.py
```

## Run locally (no Docker)
```bash
python -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
pytest -v                # run tests
flake8 .                 # lint
python wsgi.py           # http://localhost:5000
```

## Run with Docker
```bash
docker build -t sprintboard .
docker run -d -p 5000:5000 --name sprintboard sprintboard
curl http://localhost:5000/health        # {"status":"ok","version":"1.0.0"}
# or
docker compose up --build
```
Open **http://localhost:5000** in a browser.

## REST API
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check (used by CI and Docker HEALTHCHECK) |
| GET | `/api/tasks` | List tasks |
| POST | `/api/tasks` | Create task `{"title": "..."}` |
| PATCH | `/api/tasks/<id>` | Move task `{"status": "To Do" \| "In Progress" \| "Done"}` |
| DELETE | `/api/tasks/<id>` | Delete task |
| GET | `/api/summary` | Counts per column and % done |

## Pipeline (`.github/workflows/ci.yml`)
1. **build-and-test** — checkout → set up Python → install deps → `flake8` → `pytest`
2. **docker** (runs only if job 1 passes) — build image → start container → smoke-test `/health`
3. On push to `main` only — log in to GHCR with the built-in `GITHUB_TOKEN` and publish the image
   (no extra secrets needed).

## Setup steps (GitHub)
```bash
git init
git add .
git commit -m "DEV-1: initial SprintBoard application"
git branch -M main
git remote add origin https://github.com/<your-username>/sprintboard.git
git push -u origin main
```
Use Jira keys in commit messages / branch names (e.g. `feature/DEV-2-add-task-api`) so Jira can link work to issues.

## Limitations (good discussion points)
- Tasks are stored **in memory** and reset on restart; a next sprint could add SQLite/PostgreSQL.
- Single Gunicorn worker for the same reason.
- Deployment is to a local/VM Docker host; no cloud automation yet.
