from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request, status
from cron.worker import celery

app = FastAPI()


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
    task = celery.send_task('square.task', args=[number])
    return JSONResponse(content={'msg': 'success', 'id': task.id})
