import re

class Validator:
    @staticmethod
    def validate_title(title):
        pattern = r"^[A-Za-z0-9\s\-']+$"
        return bool(re.match(pattern, title))