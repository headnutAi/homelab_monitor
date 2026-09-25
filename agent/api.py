from fastapi import FastAPI
from agent.collector import collect_metrics, Metrics

app = FastAPI()


@app.get("/metrics")
def get_metrics():
    return collect_metrics()








    """TODO 1: collect_metrics() aufrufen und das Ergebnis zurückgeben.

    FastAPI kann Dataclasses direkt als Response nehmen und
    wandelt sie automatisch in JSON um – du musst also nicht
    manuell serialisieren.
    """
    pass