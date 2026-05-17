from models.base_media import BaseMedia

class Song(BaseMedia):
    def __init__(self, title, artist, genre, duration):
        super().__init__(title, artist)
        self.genre = genre
        self.duration = duration

    def play(self):
        return f"Playing {self._title}..."

    def __str__(self):
        return (
            f"{self._title} - {self._artist} "
            f"[{self.genre}] ({self.duration} sec)"
        )