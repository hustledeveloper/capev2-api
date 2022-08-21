# syntax=docker/dockerfile:1
FROM python:3.10.5-alpine

WORKDIR /app

EXPOSE 5000/tcp
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]
