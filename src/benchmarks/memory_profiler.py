import tracemalloc
from functools import wraps

def profile_memory(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Memory usage:\n"
              f"Current: {current / 10**6:.2f}MB\n"
              f"Peak: {peak / 10**6:.2f}MB")
        return result
    return wrapper
