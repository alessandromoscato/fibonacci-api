from fastapi import APIRouter, HTTPException
import math

router = APIRouter()


@router.get('/FindInFibonacci/{num}')
async def find_in_fibonacci(num: int):
    try:
        nearest_fibonacci = _nearest_fibonacci(num)
        number_before_in_series = _previous_fibonacci(nearest_fibonacci)
        number_after_in_series = _next_fibonacci(nearest_fibonacci)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'500 Internal Server Error: {e}')

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

    ### Compute Fibonacci numbers recursively. Stop when the last 
    ### computed Fibonacci number is greater than (or equal to) 
    ### the input number. This guarantees that the input number will 
    ### be between the last second and third Fibonacci numbers computed
    while (third <= num):
        first = second
        second = third
        third = first + second

    ### Return the Fibonacci number closer to the input number. If the
    ### input number is equally distanced between the last second and
    ### third Fibonacci numbers computed, return arbitrarily the second
    if (abs(third - num) >=
        abs(second - num)):
        ans = second

    else:
        ans = third

    return ans

def _next_fibonacci(num):
    if num == 0:
        return 1

    ### The ratio between two Fibonacci number converges to ((1 + sqrt(5)) / 2),
    ### so we can easily obtain the next Fibonacci number
    next_num = num * (1 + math.sqrt(5)) / 2.0
    return round(next_num)

def _previous_fibonacci(num):
    if num == 0:
        return None

    ### The ratio between two Fibonacci number converges to ((1 + sqrt(5)) / 2),
    ### so we can easily obtain the previous Fibonacci number
    previous_num = num / ((1 + math.sqrt(5)) / 2.0)
    return round(previous_num)
