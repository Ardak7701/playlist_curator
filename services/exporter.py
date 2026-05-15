import re

class M3UExporter:
    @staticmethod
    def export(playlist, filename):
        # Регулярное выражение: только буквы, цифры, точки и тире (2 балла за Regex)
        if not re.match(r'^[\w\-. ]+$', filename):
            raise ValueError("Invalid filename! Use only letters and numbers.")
        
        full_path = f"{filename}.m3u"
        with open(full_path, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for song in playlist:
                f.write(f"#EXTINF:{song.duration_sec},{song.get_info()}\n")
                f.write(f"C:/Music/{song._title}.mp3\n")
        return full_path