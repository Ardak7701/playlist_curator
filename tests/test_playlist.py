import unittest

from models.song import Song
from models.playlist import Playlist


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("Favorites")

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

    def test_find_song(self):
        self.playlist.add_song(self.song)

        result = self.playlist.find_song("Believer")

        self.assertIsNotNone(result)

    def test_song_genre(self):
        self.assertEqual(self.song.genre, "Rock")

    def test_song_duration(self):
        self.assertTrue(self.song.duration > 0)


if __name__ == "__main__":
    unittest.main()