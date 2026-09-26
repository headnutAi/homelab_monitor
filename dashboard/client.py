from datetime import datetime

import requests

from agent.collector import Metrics

DEFAULT_URL = "http://localhost:8000"


def fetch_metrics(base_url: str = DEFAULT_URL) -> Metrics:
    response = requests.get(f"{base_url}/metrics")
    response.raise_for_status()
    response_json = response.json()


    raw_timestamp = response_json.pop("timestamp")
    clean_timestamp = datetime.fromisoformat(raw_timestamp)

    results = Metrics(timestamp=clean_timestamp, **response_json)



    return results




if __name__ == "__main__":
    print(fetch_metrics())
