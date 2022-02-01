from fastapi import FastAPI, HTTPException
import math

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/api/v1/FindInFibonacci/{num}')
async def find_in_fibonacci(num: int):
    try:
        nearest_fibonacci = _nearest_fibonacci(num)
        number_before_in_series = _previous_fibonacci(nearest_fibonacci)
        number_after_in_series = _next_fibonacci(nearest_fibonacci)

    except:
        raise HTTPException(status_code=500, detail='500 Internal Server Error')

    return {
        'nearest_fibonacci': nearest_fibonacci, 
        'number_before_in_series': number_before_in_series, 
        'number_after_in_series': number_after_in_series
    }

def _nearest_fibonacci(num):

    if (num == 0):
        return 0

    first = 0
    second = 1
    third = first + second

    while (third <= num):
        first = second
        second = third
        third = first + second

    if (abs(third - num) >=
        abs(second - num)):
        ans = second

    else:
        ans = third

    return ans

def _next_fibonacci(num):
    if num == 0:
        return 1
    next_num = num * (1 + math.sqrt(5)) / 2.0
    return round(next_num)

def _previous_fibonacci(num):
    if num == 0:
        return None
    previous_num = num / ((1 + math.sqrt(5)) / 2.0)
    return round(previous_num)
