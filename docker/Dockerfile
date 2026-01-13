# ---------- Builder stage ----------
FROM python:3.10-slim AS builder

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest

COPY app ./app
COPY tests ./tests

RUN pytest tests/

# ---------- Runtime stage ----------
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY app .

EXPOSE 5000

CMD ["python", "app.py"]
