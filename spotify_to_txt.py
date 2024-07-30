import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace with your Spotify API credentials
CLIENT_ID = ' '
CLIENT_SECRET = ' '
REDIRECT_URI = 'http://localhost:8888/callback'

def get_playlist_tracks(sp, playlist_link):
    playlist_id = playlist_link.split('/')[-1].split('?')[0]
    results = sp.playlist(playlist_id)
    playlist_name = results['name']
    tracks = results['tracks']['items']

    with open(f"{playlist_name}.txt", "w", encoding="utf-8") as file:
        for idx, item in enumerate(tracks):
            track = item['track']
            file.write(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}\n")

    print(f"Playlist '{playlist_name}' has been written to {playlist_name}.txt")

def main():
    if len(sys.argv) != 2:
        print("Usage: python spotify_to_txt.py <playlist_url>")
        sys.exit(1)

    playlist_link = sys.argv[1]

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope="playlist-read-private"))

    get_playlist_tracks(sp, playlist_link)

if __name__ == "__main__":
    main()
