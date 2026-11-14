from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)
tasks = []
next_id = 1

PAGE = """<!doctype html><title>Agentic Tick</title>
<style>body{max-width:640px;margin:4rem auto;font:16px system-ui;background:#111827;color:#f8fafc}input,button{padding:.7rem;border-radius:.5rem}li{margin:.6rem 0}</style>
<h1>Agentic Tick</h1><p>Simple Flask task tracker</p>
<form id=f><input id=t placeholder="Add a task" required><button>Add</button></form><ul id=l></ul>
<script>
const api=(u,o={})=>fetch(u,{headers:{"Content-Type":"application/json"},...o}).then(r=>r.json());
async function load(){const a=await api("/api/tasks");l.innerHTML=a.map(x=>"<li>"+x.title+"</li>").join("")}
f.onsubmit=async e=>{e.preventDefault();await api("/api/tasks",{method:"POST",body:JSON.stringify({title:t.value})});t.value="";load()};load()
</script>"""

@app.get("/")
def index():
    return render_template_string(PAGE)

@app.get("/api/tasks")
def list_tasks():
    return jsonify(tasks)

@app.post("/api/tasks")
def add_task():
    global next_id
    title = (request.get_json() or {}).get("title", "").strip()
    if not title:
        return jsonify(error="A title is required"), 400
    task = {"id": next_id, "title": title}
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

if __name__ == "__main__":
    app.run(debug=True)
