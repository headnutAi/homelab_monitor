from fastapi import FastAPI

from agent.collector import collect_metrics

app = FastAPI()


@app.get("/metrics")
def get_metrics():
    return collect_metrics()