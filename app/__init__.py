"""SprintBoard - a tiny Kanban-style task tracker (Agile + DevOps mini project)."""
from threading import Lock

from flask import Flask, jsonify, render_template, request

VALID_STATUSES = ("To Do", "In Progress", "Done")


def create_app():
    app = Flask(__name__)
    store = {"tasks": {}, "next_id": 1}
    lock = Lock()

    def _add(title, status="To Do"):
        with lock:
            task = {"id": store["next_id"], "title": title, "status": status}
            store["tasks"][task["id"]] = task
            store["next_id"] += 1
            return task

    for seed_title in ("Plan the sprint", "Write unit tests", "Build Docker image"):
        _add(seed_title)

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/health")
    def health():
        return jsonify(status="ok", version="1.0.0")

    @app.get("/api/tasks")
    def list_tasks():
        return jsonify(list(store["tasks"].values()))

    @app.post("/api/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify(error="title is required"), 400
        if len(title) > 100:
            return jsonify(error="title must be 100 characters or fewer"), 400
        return jsonify(_add(title)), 201

    @app.patch("/api/tasks/<int:task_id>")
    def update_task(task_id):
        task = store["tasks"].get(task_id)
        if task is None:
            return jsonify(error="task not found"), 404
        status = (request.get_json(silent=True) or {}).get("status")
        if status not in VALID_STATUSES:
            return jsonify(error=f"status must be one of {list(VALID_STATUSES)}"), 400
        task["status"] = status
        return jsonify(task)

    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id):
        if store["tasks"].pop(task_id, None) is None:
            return jsonify(error="task not found"), 404
        return "", 204

    @app.get("/api/summary")
    def summary():
        counts = {s: 0 for s in VALID_STATUSES}
        for t in store["tasks"].values():
            counts[t["status"]] += 1
        total = sum(counts.values())
        pct = round(100 * counts["Done"] / total) if total else 0
        return jsonify(counts=counts, total=total, percent_done=pct)

    return app
