import math

from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request, status

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={'msg': exc.errors()[0]['msg']},
    )


@app.get('/square')
def get_square(number: int):
    if number <= 0:
        return JSONResponse(content={'msg': 'The number should be greater than 0'}, status_code=400)
    return JSONResponse(content={'msg': 'success', 'result': math.sqrt(number)})
