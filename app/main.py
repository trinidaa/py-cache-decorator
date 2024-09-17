from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    catcher = {}

    @wraps(func)
    def wrapper(*args: Callable) -> Callable:
        result = func(*args)
        if args in catcher:
            print("Getting from cache")
            return catcher[args]
        else:
            catcher[args] = result
            print("Calculating new result")
            return result
    return wrapper
