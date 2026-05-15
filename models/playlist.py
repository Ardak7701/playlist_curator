class Playlist:
    """
    Класс плейлиста (критерий Core OOP).
    Реализует инкапсуляцию и кастомную итерацию.
    """
    def __init__(self, name):
        self.name = name
        self.__songs = []  # Приватный список песен (Инкапсуляция)

    def add_song(self, song):
        """Метод для добавления объекта Song (Association)."""
        self.__songs.append(song)

    def get_songs(self):
        """Возвращает список песен."""
        return self.__songs

    def __iter__(self):
        """Кастомный итератор (критерий Iterators)."""
        return iter(self.__songs)