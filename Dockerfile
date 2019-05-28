FROM python:3.7-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 BROKER_URL=amqp://apigateway:gman@127.0.0.1:5672/ RESULT_BACKEND=amqp://apigateway:gman@127.0.0.1:5672/

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD celery -A main.celery worker --concurrency=4
