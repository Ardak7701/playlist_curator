class BaseMedia:
    """Базовый класс (Inheritance)."""
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist

class Song(BaseMedia):
    """Класс песни, наследующий BaseMedia."""
    def __init__(self, title, artist, genre, duration_sec):
        super().__init__(title, artist)
        self.genre = genre
        self.duration_sec = duration_sec

    def get_info(self):
        return f"{self._title} by {self._artist}"

    def __str__(self):
        return f"[{self.genre}] {self.get_info()}"