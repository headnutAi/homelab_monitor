import time
from rich.console import Console
from rich.live import Live
from rich.table import Table

from dashboard.client import fetch_metrics


def build_table(metrics) -> Table:
    table = Table(title="HomeLab Monitor Dashboard")

    table.add_column("Metrik")
    table.add_column("Wert")
    table.add_row("CPU", f"{metrics.cpu} %")
    table.add_row("Memory", f"{metrics.ram} %")
    table.add_row("Disk", f"{metrics.disk} %")

    return table


def run(refresh_seconds: float = 2.0):
    results = fetch_metrics()

    with Live(build_table(results), refresh_per_second=refresh_seconds) as live:
        while True:
            try:
                results = fetch_metrics()
                live.update(build_table(results))
                time.sleep(refresh_seconds)
            except Exception as e:
                live.console.print(f"Failed: {e}")


if __name__ == "__main__":
    run()
