FROM python:3.7-slim-buster

COPY /requirements/api.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY /app /app
COPY /cron /cron

