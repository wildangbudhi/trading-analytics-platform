FROM python:3.9.18-slim

WORKDIR /app

RUN apt-get -y update
RUN apt-get install -y python3-dev build-essential

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD [ "stdbuf", "-oL", "python3", "-u", "main.py"]
