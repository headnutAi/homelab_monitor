import os
import secrets

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import APIKeyHeader

from agent.collector import collect_metrics

load_dotenv("apiKey.env")
API_KEY = os.getenv("MONITOR_API_KEY")

if not API_KEY:
    raise RuntimeError("API key is missing")

api_key_header = APIKeyHeader(name="X-API-Key")

app = FastAPI()


def verify_api_key(key: str = Depends(api_key_header)):
    if not secrets.compare_digest(key, API_KEY):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.get("/metrics", dependencies=[Depends(verify_api_key)])
def get_metrics():
    return collect_metrics()
