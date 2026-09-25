from datetime import datetime

from agent.collector import Metrics, collect_metrics


def test_returns_metrics_object():
    results = collect_metrics()
    isinstance(results, Metrics), f"Erwartete Instanz von Metrics, aber erhielt {type(results).__name__}"

def test_values_in_valid_range():
    results = collect_metrics()
    assert 0 <= results.cpu <= 100, f"CPU-Wert außerhalb des Bereichs (0-100): {results.cpu}"
    assert 0 <= results.ram <= 100, f"RAM-Wert außerhalb des Bereichs (0-100): {results.ram}"
    assert 0 <= results.disk <= 100, f"Disk-Wert außerhalb des Bereichs (0-100): {results.disk}"

def test_timestamp_is_datetime():
    results = collect_metrics()
    assert isinstance(results.timestamp, datetime), f"Timestamp ist kein datetime-Objekt, sondern {type(results.timestamp).__name__}"