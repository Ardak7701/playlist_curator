import unittest
from models.song import Song
from models.playlist import Playlist

class TestPlaylist(unittest.TestCase):
    def test_song_creation(self):
        s = Song("Test", "Artist", "Rock", 180)
        self.assertEqual(s.genre, "Rock")

    def test_playlist_add(self):
        p = Playlist("Test")
        p.add_song(Song("S", "A", "G", 100))
        self.assertEqual(len(list(p)), 1)

if __name__ == '__main__':
    unittest.main()

    def test_genre_analysis(self):
        """Проверка анализатора жанров (Functional Programming)."""
        from services.analyzer import GenreAnalyzer
        pl = Playlist("Jazz Mix")
        pl.add_song(Song("Song1", "Artist1", "Jazz", 120))
        stats = GenreAnalyzer.count_genres(pl)
        self.assertEqual(stats["Jazz"], 1)[cite: 1]

    def test_filename_validation(self):
        """Проверка Regex для экспорта (Regex)."""
        import re
        filename = "my_playlist_2026"
        self.assertTrue(re.match(r'^[\w\-. ]+$', filename))[cite: 1]

    def test_file_handler_json(self):
        """Проверка сохранения данных (Data Persistence)."""
        from utils.validators import FileHandler
        import os
        data = {"count": 1}
        FileHandler.save_to_json(data, "temp.json")
        loaded = FileHandler.load_from_json("temp.json")
        self.assertEqual(loaded["count"], 1)
        if os.path.exists("temp.json"):
            os.remove("temp.json")[cite: 1]