import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import youtube_dl

# Replace with your Spotify API credentials
CLIENT_ID = 'bc3d7434dda447899fce87f89abd32e6'
CLIENT_SECRET = 'd1b4a84dbd5440e9a5b93c681b425cc4'
REDIRECT_URI = 'http://localhost:8888/callback'

def get_spotify_tracks(sp, playlist_link):
    playlist_id = playlist_link.split('/')[-1].split('?')[0]
    results = sp.playlist(playlist_id)
    playlist_name = results['name']
    tracks = results['tracks']['items']
    track_list = [(track['track']['name'], track['track']['artists'][0]['name']) for track in tracks]
    return playlist_name, track_list

def get_youtube_music_tracks(youtube_playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_playlist_url, download=False)
        track_list = [(entry['title'], entry.get('artist', 'Unknown')) for entry in info_dict['entries']]
    return track_list

def normalize_track_name(track_name):
    return track_name.lower().replace(" ", "")

def write_tracks_to_file(filename, tracks):
    with open(filename, "w", encoding="utf-8") as file:
        for idx, (track_name, artist_name) in enumerate(tracks):
            file.write(f"{idx + 1}. {track_name} - {artist_name}\n")

def write_unique_tracks_to_file(filename, tracks):
    with open(filename, "w", encoding="utf-8") as file:
        for idx, (track_name, artist_name) in enumerate(tracks):
            file.write(f"{idx + 1}. {track_name} - {artist_name}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python spotify_to_txt.py <spotify_playlist_url> <youtube_music_playlist_url>")
        sys.exit(1)

    spotify_playlist_link = sys.argv[1]
    youtube_playlist_link = sys.argv[2]

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope="playlist-read-private"))

    playlist_name, spotify_tracks = get_spotify_tracks(sp, spotify_playlist_link)
    youtube_tracks = get_youtube_music_tracks(youtube_playlist_link)

    # Normalize track names
    spotify_track_names = {normalize_track_name(name): (name, artist) for name, artist in spotify_tracks}
    youtube_track_names = {normalize_track_name(name) for name, artist in youtube_tracks}

    # Find unique tracks
    unique_tracks = [(name, artist) for norm_name, (name, artist) in spotify_track_names.items() if norm_name not in youtube_track_names]

    write_tracks_to_file(f"{playlist_name}_spotify.txt", spotify_tracks)
    write_tracks_to_file("youtube_music_tracks.txt", youtube_tracks)
    write_unique_tracks_to_file(f"{playlist_name}_unique.txt", unique_tracks)

    print(f"Tracks from Spotify playlist written to {playlist_name}_spotify.txt")
    print(f"Tracks from YouTube Music playlist written to youtube_music_tracks.txt")
    print(f"Unique tracks written to {playlist_name}_unique.txt")

if __name__ == "__main__":
    main()
