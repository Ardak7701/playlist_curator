class Playlist:
    def __init__(self, name):
        self.name = name
        self.__songs = []

    def add_song(self, song):
        self.__songs.append(song)

    def remove_song(self, title):
        self.__songs = [
            song for song in self.__songs
            if song._title != title
        ]

    def get_songs(self):
        return self.__songs

    def __iter__(self):
        return iter(self.__songs)

    def __len__(self):
        return len(self.__songs)