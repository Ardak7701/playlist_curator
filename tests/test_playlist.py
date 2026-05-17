import unittest

from models.song import Song
from models.playlist import Playlist


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("Test Playlist")

        self.song = Song(
            "Believer",
            "Imagine Dragons",
            "Rock",
            204
        )

    def test_add_song(self):
        self.playlist.add_song(self.song)
        self.assertEqual(len(self.playlist), 1)
    
    def test_remove_song(self):
        self.playlist.add_song(self.song)
        self.playlist.remove_song("Believer")
        self.assertEqual(len(self.playlist), 0)

    def test_song_title(self):
        self.assertEqual(self.song._title, "Believer")

    def test_song_genre(self):
        self.assertTrue(self.song.genre == "Rock")

    def test_playlist_iteration(self):
        self.playlist.add_song(self.song)

        for item in self.playlist:
            self.assertEqual(item._title, "Believer")


if __name__ == "__main__":
    unittest.main()