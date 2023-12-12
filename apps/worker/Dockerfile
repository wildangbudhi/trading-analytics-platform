FROM python:3.9.18-slim

WORKDIR /app

RUN apt-get -y update
RUN apt-get install -y python3-dev build-essential libpq-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["celery", "-A", "worker.app", "worker", "-l", "INFO"]
