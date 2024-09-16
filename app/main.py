from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    catcher = set()

    @wraps(func)
    def wrapper(*args: Callable) -> Callable:
        result = func(*args)
        # Преобразуем результат в кортеж, чтобы избежать ошибки "unhashable type"
        result_tuple = tuple(result) if isinstance(result, list) else result
        if result_tuple in catcher:
            print("Getting from cache")
            return result
        else:
            catcher.add(result_tuple)
            print("Calculating new result")
            return result

    return wrapper
