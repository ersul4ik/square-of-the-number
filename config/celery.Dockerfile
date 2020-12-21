FROM python:3.7-slim-buster

COPY /requirements/celery.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY /cron /celery_tasks
WORKDIR /celery_tasks

ENTRYPOINT celery -A tasks worker -c 4 --loglevel=info
