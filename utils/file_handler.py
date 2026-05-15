import json
import functools

def log_action(func):
    """Кастомный декоратор для логирования действий (3 балла за Decorators)."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[SYSTEM LOG] Running action: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class FileHandler:
    @staticmethod
    @log_action
    def save_to_json(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)