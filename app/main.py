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
            print(f"Symbol(s) > {result_tuple} < detect duplicate. Stopping cache!")
            return result
        else:
            catcher.add(result_tuple)
            print(f"Caching result: {result_tuple}.")
            return result
    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[Any]:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)

# Calculating new result
# Calculating new result
# Calculating new result
# Getting from cache
# Calculating new result
# Getting from cache