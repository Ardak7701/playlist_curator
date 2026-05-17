import json
import csv
import os

from models.song import Song
class StorageManager:
    """
    Handles JSON and CSV storage.
    """

    @staticmethod
    def save_to_json(playlist, filename="data/playlist.json"):
        os.makedirs("data", exist_ok=True)

        data = []

        for song in playlist:
            data.append({
                "title": song._title,
                "artist": song._artist,
                "genre": song.genre,
                "duration": song.duration
            })

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Playlist saved to JSON successfully.")

    @staticmethod
    def load_from_json(filename="data/playlist.json"):
        songs = []

        if not os.path.exists(filename):
            return songs

        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            songs.append(
                Song(
                    item["title"],
                    item["artist"],
                    item["genre"],
                    item["duration"]
                )
            )

        return songs
    
    @staticmethod
    def export_to_csv(playlist, filename="data/playlist.csv"):
        os.makedirs("data", exist_ok=True)

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Title",
                "Artist",
                "Genre",
                "Duration"
            ])

            for song in playlist:
                writer.writerow([
                    song._title,
                    song._artist,
                    song.genre,
                    song.duration
                ])
        print("Playlist exported to CSV successfully.")