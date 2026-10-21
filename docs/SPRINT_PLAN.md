# SprintBoard — Agile Plan (Scrum)

## 1. Product vision
> For student teams who need a lightweight way to see work in progress, SprintBoard is a web-based
> Kanban board that shows tasks moving from **To Do → In Progress → Done**, delivered through an
> automated DevOps pipeline.

## 2. Team roles (Scrum)
| Role | Responsibility |
|---|---|
| Product Owner | Owns and prioritises the backlog, accepts stories |
| Scrum Master | Facilitates ceremonies, removes blockers |
| Developers | Build, test, containerise and deploy |

*(In a solo/pair mini-project, one person may hold several roles — state this in your report.)*

## 3. Product backlog (user stories)
Priority: **H**igh / **M**edium / **L**ow. Estimates in story points (Fibonacci).

| ID | User story | Acceptance criteria | Priority | Pts |
|---|---|---|---|---|
| US-1 | As a user, I want to see tasks in three columns so I know the status of work. | Board shows To Do / In Progress / Done; seeded tasks visible | H | 3 |
| US-2 | As a user, I want to add a task so I can capture new work. | Empty or >100-char titles rejected (HTTP 400); new task appears in To Do | H | 3 |
| US-3 | As a user, I want to move a task between columns so I can show progress. | Only valid statuses accepted; unknown id → 404 | H | 3 |
| US-4 | As a user, I want to delete a task so the board stays clean. | Task removed; repeat delete → 404 | M | 2 |
| US-5 | As a user, I want a progress summary so I can see % complete. | `/api/summary` returns counts and % done | M | 2 |
| US-6 | As a developer, I want automated tests and lint on every push so defects are caught early. | CI fails on lint/test error | H | 5 |
| US-7 | As an operator, I want a Docker image so the app runs the same everywhere. | Image builds; container passes `/health` | H | 3 |
| US-8 | As an operator, I want the image published automatically from `main`. | Image visible in GHCR after merge | L | 3 |

## 4. Definition of Done
- Code reviewed via pull request and merged to `main`
- Unit tests written and passing; flake8 clean
- CI pipeline green (build, test, Docker build, smoke test)
- Acceptance criteria demonstrated in browser
- Jira issue moved to **Done**

## 5. Sprint plan
### Sprint 1 (Week 1) — "Working application"  · Goal: usable board running locally
US-1, US-2, US-3, US-4, US-5 → **13 pts**

### Sprint 2 (Week 2) — "Automated delivery" · Goal: every push is built, tested and packaged
US-6, US-7, US-8 → **11 pts**

### Scrum ceremonies
| Ceremony | When | Output |
|---|---|---|
| Sprint planning | Start of sprint | Sprint backlog and goal |
| Daily stand-up | Daily (15 min) | Yesterday / today / blockers |
| Sprint review | End of sprint | Demo in browser |
| Retrospective | End of sprint | 1–3 improvement actions |

## 6. Jira issues to create (matches the lab's DEV-01…DEV-05 pattern)
Create a **Scrum** project with key `DEV`. Create an **Epic** "SprintBoard MVP" and link the issues below.

| Key | Type | Summary | Sprint | Story | Status to demo |
|---|---|---|---|---|---|
| DEV-1 | Task | Create GitHub repository and project skeleton | 1 | – | Done |
| DEV-2 | Story | Show Kanban board with three columns | 1 | US-1 | Done |
| DEV-3 | Story | Add-task API with validation | 1 | US-2 | Done |
| DEV-4 | Story | Move task between columns | 1 | US-3 | Done |
| DEV-5 | Story | Delete task | 1 | US-4 | Done |
| DEV-6 | Story | Progress summary endpoint | 1 | US-5 | Done |
| DEV-7 | Task | Configure pytest and flake8 in GitHub Actions | 2 | US-6 | In Progress |
| DEV-8 | Task | Create Dockerfile and docker-compose | 2 | US-7 | To Do |
| DEV-9 | Task | Publish image to GHCR from `main` | 2 | US-8 | To Do |
| DEV-10 | Bug | *(Optional demo)* Title with only spaces accepted | 2 | US-2 | Done |
| DEV-11 | Task | Deploy container and verify in browser | 2 | – | To Do |

> Replace the statuses with **your real** statuses when you take screenshots.

### Suggested workflow columns
`To Do → In Progress → In Review → Done`

## 7. Git workflow tied to Jira
1. Pick issue `DEV-3` from the sprint board and move it to **In Progress**.
2. `git checkout -b feature/DEV-3-add-task-api`
3. Commit: `DEV-3: validate task title length`
4. Push and open a **pull request** → CI runs automatically.
5. When CI is green and reviewed, merge → move issue to **Done**.

## 8. Burndown tracking (fill in during the sprint)
| Day | Points remaining (Sprint 1, start = 13) |
|---|---|
| 1 | 13 |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |

## 9. Retrospective template
| Went well | Could improve | Action for next sprint |
|---|---|---|
|  |  |  |
