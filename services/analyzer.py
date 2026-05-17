from collections import Counter

class GenreAnalyzer:
    """
    Provides playlist analysis functionality.
    """

    @staticmethod
    def analyze_genres(playlist):
        genres = list(
            map(lambda song: song.genre, playlist)
        )

        return Counter(genres)

    @staticmethod
    def filter_by_genre(playlist, genre):
        return list(
            filter(
                lambda song: song.genre.lower() == genre.lower(),
                playlist
            )
        )