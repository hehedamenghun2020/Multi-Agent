from fastapi import FastAPI
from app.workflow.engine import WorkflowEngine

app = FastAPI()
engine = WorkflowEngine()

@app.get("/run")
def run(task: str):
    return {"result": engine.run(task)}
