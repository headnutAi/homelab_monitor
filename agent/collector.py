from dataclasses import dataclass, field
from datetime import datetime

import psutil


@dataclass
class Metrics:
    cpu: float
    ram: float
    disk: float
    timestamp: datetime = field(default_factory=datetime.now)


def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    temp = Metrics(cpu=cpu, ram=ram, disk=disk)

    return temp

if __name__ == '__main__':
    metrics = collect_metrics()
    print(f"CPU: {metrics.cpu}")
    print(f"RAM: {metrics.ram}")
    print(f"DISK: {metrics.disk}")
    print(f"TIMESTAMP: {metrics.timestamp}")


