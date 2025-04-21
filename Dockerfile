FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir numpy

CMD ["python", "bb84.py"]
