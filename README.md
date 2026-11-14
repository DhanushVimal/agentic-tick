# Agentic Tick

A compact full-stack Flask task tracker with a browser interface and JSON API.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000.

## API

- `GET /api/tasks` lists tasks
- `POST /api/tasks` adds a task using `{"title":"..." }`
