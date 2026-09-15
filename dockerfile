FROM python:3.11-slim

WORKDIR /app

COPY analyzer.py .
COPY sample.log .

ENTRYPOINT ["python", "analyzer.py"]
