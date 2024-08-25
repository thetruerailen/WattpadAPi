
import time
from functools import wraps
from ..exceptions import RateLimitError

def rate_limit(max_calls, time_frame):
    def decorator(func):
        calls = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls[:] = [c for c in calls if c > now - time_frame]
            if len(calls) >= max_calls:
                raise RateLimitError(f"Rate limit of {max_calls} calls per {time_frame} seconds exceeded")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator
