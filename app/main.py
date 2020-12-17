from fastapi import FastAPI
from fastapi.responses import JSONResponse


# Create the FastAPI app
app = FastAPI()


@app.get('/square')
def get_square(number: int):
    if number <= 0:
        return JSONResponse(content={'message': 'The number should be greater than 0'}, status_code=400)
    return JSONResponse(content={'message': number})
