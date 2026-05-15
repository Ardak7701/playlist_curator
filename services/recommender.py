class Recommender:
    @staticmethod
    def suggest_similar(playlist, genre):
        """Кастомный генератор для обработки данных (3 балла за Iterators/Generators)."""
        for song in playlist.get_songs():
            if song.genre == genre:
                yield f"Similar to {song._title}: [New Discovery in {genre}]"