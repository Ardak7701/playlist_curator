class PlaylistExporter:
    """
    Exports playlist into M3U format.
    """

    @staticmethod
    def export_to_m3u(playlist, filename="playlist.m3u"):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("#EXTM3U\n")

            for song in playlist:
                file.write(
                    f"#EXTINF:{song.duration},"
                    f"{song._artist} - {song._title}\n"
                )

        print(f"Playlist exported to {filename}")