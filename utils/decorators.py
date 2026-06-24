import logging
from time import perf_counter


def log_execution(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        logging.info(
            "Function %s executed in %.4f seconds with result: %s",
            func.__name__,
            elapsed,
            result,
        )
        return result

    return wrapper
