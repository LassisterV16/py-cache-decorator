from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    results_of_completed_runs = {}

    @wraps(func)
    def wrapper(*args) -> int:
        if not results_of_completed_runs.get(wrapper.__name__):
            results_of_completed_runs[wrapper.__name__] = {}

        if (results_of_completed_runs[wrapper.__name__].get(args)
                or results_of_completed_runs[wrapper.__name__].get(args) == 0):
            print("Getting from cache")
            return results_of_completed_runs[wrapper.__name__][args]
        else:
            result_of_run = func(*args)
            results_of_completed_runs[wrapper.__name__][args] = result_of_run
            print("Calculating new result")
            return result_of_run

    return wrapper
