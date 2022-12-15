# Separate build image
FROM python:3.9-slim as builder

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN apt-get update \
     && apt-get install -y gcc \
     && pip install --no-cache-dir --upgrade pip \
     && pip install --no-cache-dir setuptools wheel \
     && pip install --no-cache-dir -r requirements.txt \
     && rm -rf /var/lib/apt/lists/*

# Final image
FROM python:3.9-slim
COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY alembic.ini /app/alembic.ini

COPY alembic /app/alembic

COPY bot /app/bot
#CMD ["python", "-u", "bot"]
