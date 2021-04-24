from time import time
from typing import Callable, Any, Tuple, Dict


def timer(f: Callable) -> Callable:
    def inner(*args, **kwargs) -> Tuple[Any, float]:
        start = time()
        results = f(*args, **kwargs)
        end = time()
        return results, (end-start)
    inner.__name__ = f.__name__
    return inner


def num_used_colours(results: Dict[int, int]) -> int:
    return len(set(results.values()))
