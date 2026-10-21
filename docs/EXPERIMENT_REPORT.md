# EXPERIMENT NO. 10
## Design and Implementation of an End-to-End DevOps Pipeline through a Mini Project
**Subject:** Agile Software Development and DevOps

| | |
|---|---|
| Name | ______________________ |
| Roll Number | ______________________ |
| Class / Division | ______________________ |
| Department | ______________________ |
| Academic Year | ______________________ |
| Project | SprintBoard — Kanban task tracker |
| GitHub repo | https://github.com/<username>/sprintboard |

## 1. Aim
To design and implement an end-to-end DevOps pipeline through a mini project by managing work in Jira, maintaining source code in GitHub, automating build and test steps with GitHub Actions, packaging the application using Docker, and verifying the deployed application.

## 2. Objectives
- Understand the stages of the DevOps lifecycle.
- Plan and track work using Jira issues and a Scrum board.
- Store and manage source code using Git and GitHub.
- Automate build and test using a CI/CD workflow.
- Package the application in a Docker container.
- Deploy and verify the application.
- Understand how planning, development, testing and deployment work together.

## 3. Tools Used
| Tool | Use in this project |
|---|---|
| Jira | Scrum board, user stories, sprints, bug tracking |
| Git / GitHub | Version control, pull requests, repository hosting |
| GitHub Actions | CI: lint, unit tests, Docker build, smoke test, image publish |
| Docker | Containerising the Flask app |
| VS Code, browser | Development and verification |
| Python 3.12, Flask, pytest, flake8 | Application, tests, static analysis |

## 4. Theory
DevOps combines development and operations practices to improve collaboration, automation and the reliability of software delivery. Agile (Scrum) supplies the planning rhythm — short sprints, a prioritised backlog and frequent reviews — while DevOps supplies the automation that makes each sprint's output releasable.

An end-to-end pipeline links source control, building, testing, packaging, deployment and verification. Jira plans and tracks the work (it does not run builds). GitHub stores code and triggers GitHub Actions on push or pull request. GitHub Actions executes the automated workflow, and Docker packages the app and dependencies into a portable container.

```
Plan → Code → Build → Test → Package → Deploy → Verify
Jira → GitHub → GitHub Actions → Docker → Target Environment
```

## 5. Project Description
SprintBoard is a web app with a REST API and a three-column Kanban UI (To Do / In Progress / Done). Users can add, move and delete tasks and see percent complete. The backlog, sprint plan and Jira issues are in `docs/SPRINT_PLAN.md`.

## 6. System Architecture
```
Jira (Plan and Track: backlog, sprints, issues)
        ↓
Developer → git push / pull request → GitHub Repository
        ↓
GitHub Actions
   Job 1: flake8 + pytest
   Job 2: docker build → run container → curl /health
        ↓ (main branch only)
GHCR container registry → Docker host / VM
        ↓
Browser verification → update Jira issues
```

## 7. Procedure (as performed)
1. Created Jira Scrum project `DEV`, an epic "SprintBoard MVP" and the issues DEV-1…DEV-11.
2. Planned Sprint 1 (application) and Sprint 2 (automation); set priorities, story points and assignees.
3. Created the GitHub repository and pushed the Flask application and tests.
4. Added the `Dockerfile` (non-root user, Gunicorn, HEALTHCHECK) and `docker-compose.yml`.
5. Created `.github/workflows/ci.yml` to checkout, lint, run tests, build the image and smoke-test it.
6. Added a publish step that pushes the image to GHCR on `main` using the built-in `GITHUB_TOKEN`.
7. Ran the container locally (`docker run -p 5000:5000 sprintboard`).
8. Opened http://localhost:5000, added a task, moved it across columns, and checked `/health`.
9. Moved Jira issues to **Done** and recorded results below.

## 8. Key Files
- `app/__init__.py` — Flask application factory and API
- `tests/test_app.py` — 13 unit tests (success and validation cases)
- `Dockerfile` — container definition
- `.github/workflows/ci.yml` — CI pipeline

## 9. Testing and Verification
| Test | Verification method | Expected | Result *(fill in)* |
|---|---|---|---|
| Repository check | Source visible on GitHub | Files present | |
| CI workflow check | Actions tab after push / PR | Workflow triggers | |
| Build and test | Review job logs | flake8 clean; 13 tests pass | |
| Docker build | `docker images` / job log | Image `sprintboard` created | |
| Deployment check | Open http://localhost:5000 | Board loads; add/move/delete work | |
| Health check | `curl localhost:5000/health` | `{"status":"ok",...}` | |
| Jira tracking | Board after sprint | Issues reflect completed work | |

*(Local run before submission: flake8 clean and 13/13 pytest tests passed.)*

## 10. Result
Enter your actual outcome after running the workflow, e.g.: "The CI pipeline ran successfully on push to `main`; all 13 tests passed, the Docker image was built and the container responded on `/health`. The application was verified in the browser and Jira issues DEV-1 to DEV-11 were updated."

## 11. Conclusion
The experiment shows how Agile planning and DevOps automation fit together in one workflow. Jira provides visibility of tasks and sprint progress, GitHub manages source code and review, GitHub Actions automates lint, test and build, and Docker provides consistent packaging. The pipeline can be extended with a database, automated deployment to a cloud server, security scanning (e.g. Trivy, Dependabot) and monitoring.

## 12. Screenshots to Attach
1. Jira backlog and sprint board with issues and statuses
2. Jira board after updating completed tasks (burndown optional)
3. GitHub repository and source code
4. GitHub Actions workflow run with both jobs green, and logs
5. Docker image list / running container (`docker ps`)
6. SprintBoard running in the browser
