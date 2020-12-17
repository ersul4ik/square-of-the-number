import math

from worker import celery


@celery.task(name='square.task', bind=True)
def calculate_square_root(number):
    return math.sqrt(number)
