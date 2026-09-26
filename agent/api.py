import os
import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.openapi.models import APIKey
from fastapi.security import APIKeyHeader

from agent.collector import collect_metrics

API_KEY = os.getenv("MONITOR_API_KEY")
api_key_header = APIKeyHeader(name="X-API-Key")

app = FastAPI()


def verify_api_key(key: str = Depends(api_key_header)):


    """TODO 1: Vergleiche key mit API_KEY.

    - Bei Nichtübereinstimmung: HTTPException werfen mit
      status_code=status.HTTP_401_UNAUTHORIZED
    - Zum Vergleich secrets.compare_digest(key, API_KEY) nutzen,
      nicht ==
    """
    pass


@app.get("/metrics", dependencies=[Depends(verify_api_key)])
def get_metrics():
    return collect_metrics()