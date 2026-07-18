FROM python:3.10.16-slim@sha256:<APPROVED_SHA256_DIGEST>

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app
COPY access.log /app/access.log
