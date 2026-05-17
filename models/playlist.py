class Playlist:
    """
    Playlist class containing Song objects.
    Demonstrates encapsulation, iterators, generators,
    collections, and association.
    """

    def __init__(self, name):
        self.name = name
        self.__songs = []

    @property
    def songs(self):
        """Getter for songs."""
        return self.__songs

    def add_song(self, song):
        self.__songs.append(song)

    def remove_song(self, title):
        self.__songs = [
            song for song in self.__songs
            if song._title.lower() != title.lower()
        ]

    def get_songs(self):
        return self.__songs

    def find_song(self, title):
        for song in self.__songs:
            if song._title.lower() == title.lower():
                return song

        return None

    def unique_genres(self):
        """
        Demonstrates set usage.
        """
        return set(song.genre for song in self.__songs)

    def song_titles_tuple(self):
        """
        Demonstrates tuple usage.
        """
        return tuple(song._title for song in self.__songs)

    def long_songs_generator(self, minimum_duration):
        """
        Custom generator.
        """
        for song in self.__songs:
            if song.duration >= minimum_duration:
                yield song

    def __iter__(self):
        return iter(self.__songs)

    def __len__(self):
        return len(self.__songs)