import json
import os

from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request, status
from cron.worker import celery

app = FastAPI()
HOST_URL = os.getenv('HOST_URL', 'http://127.0.0.1:5050')


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """The function just for overriding the response of validation exception"""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={'msg': exc.errors()[0]['msg']},
    )


@app.get('/square')
def create_task(request: Request, number: int):
    if number <= 0:
        return JSONResponse(content={'msg': 'The number should be greater than 0'}, status_code=400)
    task = celery.send_task('square.task', kwargs={'number': number})
    result_url = f'{HOST_URL}/task/{task.id}'
    return JSONResponse(content={'msg': 'success', 'id': task.id, 'result_url': result_url})


@app.get('/task/{_id}')
def get_task(_id: str):
    task = celery.AsyncResult(_id)
    if task.state == 'SUCCESS':
        return {'status': task.state, 'result': task.result}
    elif task.state == 'FAILURE':
        response = json.loads(task.backend.get(task.backend.get_key_for_task(task.id)).decode('utf-8'))
        del response['children']
        del response['traceback']
    else:
        response = {'status': task.state, 'result': task.info}
    return response
