import os
from celery import Celery

CELERY_BROKER_URL = os.getenv('REDIS_SERVER', 'redis://redis_server:6379')
CELERY_RESULT_BACKEND = os.getenv('REDIS_SERVER', 'redis://redis_server:6379')

celery = Celery('celery', backend=CELERY_BROKER_URL, broker=CELERY_RESULT_BACKEND)
