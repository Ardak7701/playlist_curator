class GenreAnalyzer:
    @staticmethod
    def count_genres(playlist):
        genres = list(map(lambda s: s.genre, playlist))
        return {g: genres.count(g) for g in set(genres)}

# services/exporter.py
import re

class M3UExporter:
    @staticmethod
    def export(playlist, filename):
        # Regex for valid filename (2 pts)
        if not re.match(r'^[\w\-. ]+$', filename):
            raise ValueError("Invalid filename format")
        
        with open(f"{filename}.m3u", "w") as f:
            f.write("#EXTM3U\n")
            for song in playlist:
                f.write(f"#EXTINF:{song.duration_sec},{song.get_info()}\n")
                f.write(f"C:/Music/{song._title}.mp3\n")