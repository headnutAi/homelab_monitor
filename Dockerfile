FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY agent/ ./agent/
RUN adduser -D noright
USER noright
CMD ["uvicorn", "agent.api:app", "--host", "0.0.0.0", "--port", "8090"]
