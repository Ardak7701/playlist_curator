from functools import wraps

def log_action(func):
    """
    Custom decorator for logging actions.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Starting: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] Finished: {func.__name__}\n")

        return result

    return wrapper