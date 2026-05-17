class BaseMedia:
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist

    def play(self):
        raise NotImplementedError("Subclasses must implement play()")

    def __str__(self):
        return f"{self._title} by {self._artist}"