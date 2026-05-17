from models.song import Song
from models.playlist import Playlist

from services.analyzer import GenreAnalyzer
from services.exporter import PlaylistExporter
from services.storage import StorageManager
(())
from utils.decorators import log_action
from utils.validators import Validator


@log_action
def main():
    playlist = Playlist("My Playlist")

    while True:
        print("\n=== PLAYLIST CURATOR ===")
        print("1. Add song")
        print("2. Remove song")
        print("3. Show playlist")
        print("4. Analyze genres")
        print("5. Export to M3U")
        print("6. Save to JSON")
        print("7. Export to CSV")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Song title: ")

            if not Validator.validate_title(title):
                print("Invalid song title.")
                continue

            artist = input("Artist: ")
            genre = input("Genre: ")

            try:
                duration = int(input("Duration (seconds): "))

            except ValueError:
                print("Duration must be a number.")
                continue

            song = Song(title, artist, genre, duration)

            playlist.add_song(song)

            print("Song added successfully.")

        elif choice == "2":
            title = input("Enter title to remove: ")

            playlist.remove_song(title)

            print("Song removed successfully.")

        elif choice == "3":
            if len(playlist) == 0:
                print("Playlist is empty.")

            else:
                print("\nPlaylist songs:")

                for song in playlist:
                    print(song)

        elif choice == "4":
            stats = GenreAnalyzer.analyze_genres(playlist)

            print("\nGenre statistics:")

            for genre, count in stats.items():
                print(f"{genre}: {count}")

        elif choice == "5":
            PlaylistExporter.export_to_m3u(playlist)

        elif choice == "6":
            StorageManager.save_to_json(playlist)

        elif choice == "7":
            StorageManager.export_to_csv(playlist)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()