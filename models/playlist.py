class Playlist:
    """
    Playlist class containing Song objects.
    Demonstrates encapsulation and iterators.
    """
    def __init__(self, name):
        self.name = name
        self.__songs = []

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

    def __iter__(self):
        return iter(self.__songs)

    def __len__(self):
        return len(self.__songs)