import cProfile
import pstats
from functools import wraps

def profile_compilation(output_file='compilation_profile.stats'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            profiler = cProfile.Profile()
            result = profiler.runcall(func, *args, **kwargs)
            profiler.dump_stats(output_file)
            
            # Print top 10 time-consuming operations
            stats = pstats.Stats(output_file)
            stats.sort_stats('cumulative').print_stats(10)
            
            return result
        return wrapper
    return decorator
