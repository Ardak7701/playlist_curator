from models.song import Song
from models.playlist import Playlist
from services.analyzer import GenreAnalyzer
from services.exporter import M3UExporter
from services.storage import Recommender
from utils.validators import FileHandler

def main():
    my_playlist = Playlist("My Final Project Playlist")
    
    while True:
        print("\n" + "="*30)
        print("  PLAYLIST CURATOR SYSTEM  ")
        print("="*30)
        print("1. Add New Song")
        print("2. View Genre Analysis")
        print("3. Get Recommendations")
        print("4. Export to M3U")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            try:
                title = input("Enter song title: ")
                artist = input("Enter artist name: ")
                genre = input("Enter genre: ")
                duration = int(input("Enter duration in seconds: "))
                
                new_song = Song(title, artist, genre, duration)
                my_playlist.add_song(new_song)
                print(f"Successfully added: {new_song}")
            except ValueError:
                print("Error: Duration must be a number!")

        elif choice == '2':
            stats = GenreAnalyzer.count_genres(my_playlist)
            print("\nGenre Breakdown:")
            for genre, count in stats.items():
                print(f"- {genre}: {count} songs")

        elif choice == '3':
            search_genre = input("Enter genre to find similar songs: ")
            print("\nRecommendations:")
            # Использование генератора (Iterators/Generators)
            recommendations = list(Recommender.suggest_similar(my_playlist, search_genre))
            if recommendations:
                for rec in recommendations:
                    print(f"  {rec}")
            else:
                print("No songs found in this genre yet.")

        elif choice == '4':
            try:
                fname = input("Enter filename for export (e.g., 'my_hits'): ")
                path = M3UExporter.export(my_playlist, fname)
                print(f"Playlist exported successfully to {path}!")
            except ValueError as e:
                print(f"Export Error: {e}")

        elif choice == '5':
            print("Shutting down. Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()