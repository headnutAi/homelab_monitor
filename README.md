# 📊 homelab-monitor

> Leichtgewichtiges Monitoring für das eigene Homelab – ein Agent sammelt Systemmetriken, ein Dashboard zeigt sie an.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Status](https://img.shields.io/badge/Status-in%20Entwicklung-orange)

---

## Über das Projekt

`homelab-monitor` überwacht die Auslastung eines selbst gehosteten Ubuntu-Servers. Statt einer schwergewichtigen Monitoring-Suite (Prometheus, Grafana & Co.) verfolgt dieses Projekt einen bewusst minimalen Ansatz: ein kleiner Agent auf dem Server, ein schlanker Client auf dem Rechner davor.

Entstanden als Teil meines [secure-homelab](https://github.com/headnutAi/secure-homelab)-Setups.

## Architektur

```
┌──────────────────────┐          HTTP/JSON         ┌──────────────────────┐
│   Homelab-Server     │ ────────────────────────▶  │     Dashboard        │
│                      │       GET /metrics         │                      │
│  agent/collector.py  │                            │  dashboard/client.py │
│  agent/api.py        │                            │  dashboard/display.py│
└──────────────────────┘                            └──────────────────────┘
       psutil                                              rich
```

Der **Agent** läuft auf dem zu überwachenden Server und stellt die Metriken über einen HTTP-Endpoint bereit. Das **Dashboard** kann auf einem beliebigen Gerät im Netzwerk laufen und fragt den Endpoint zyklisch ab.

## Features

- ✅ Erfassung von CPU-, RAM- und Disk-Auslastung via `psutil`
- ✅ REST-Endpoint `/metrics` mit automatischer JSON-Serialisierung
- ✅ Interaktive API-Doku unter `/docs` (Swagger, von FastAPI generiert)
- 🚧 Terminal-Dashboard mit Live-Aktualisierung
- 📋 Historie der Messwerte in SQLite
- 📋 Web-Dashboard mit Verlaufsdiagrammen
- 📋 Alerting bei Schwellenwertüberschreitung

## Tech-Stack

| Komponente | Verwendung |
|---|---|
| **FastAPI** | REST-API des Agents |
| **Uvicorn** | ASGI-Server |
| **psutil** | Auslesen der Systemmetriken |
| **requests** | HTTP-Client des Dashboards |
| **rich** | Darstellung im Terminal |

## Installation

```bash
git clone https://github.com/headnutAi/homelab-monitor.git
cd homelab-monitor

python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Verwendung

### Agent starten

Auf dem zu überwachenden Server, aus dem Projekt-Root heraus:

```bash
uvicorn agent.api:app --host 0.0.0.0 --port 8000
```

Anschließend erreichbar unter:

- `http://<server-ip>:8000/metrics` – Metriken als JSON
- `http://<server-ip>:8000/docs` – interaktive API-Dokumentation

### Beispiel-Response

```json
{
  "cpu": 12.4,
  "ram": 63.8,
  "disk": 41.2,
  "timestamp": "2026-09-25T18:42:11.204Z"
}
```

## Projektstruktur

```
homelab-monitor/
├── agent/
│   ├── __init__.py
│   ├── collector.py      # sammelt Metriken (psutil)
│   └── api.py            # stellt sie als JSON bereit (FastAPI)
├── dashboard/
│   ├── client.py         # fragt den Agent ab
│   └── display.py        # Darstellung
├── requirements.txt
└── README.md
```

## Roadmap

- [x] Metrik-Erfassung mit Dataclass-Modell
- [x] FastAPI-Endpoint
- [ ] Dashboard-Client
- [ ] Live-Anzeige im Terminal (`rich`)
- [ ] Deployment als `systemd`-Service
- [ ] Absicherung des Endpoints (API-Key)
- [ ] Persistenz der Messwerte

## Hinweis zur Sicherheit

Der Agent ist aktuell **nicht authentifiziert** und sollte ausschließlich in einem vertrauenswürdigen lokalen Netzwerk betrieben werden. Eine Absicherung des Endpoints steht auf der Roadmap.

---

*Lernprojekt – Feedback und Anregungen jederzeit willkommen.*
