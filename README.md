## Python Script Logic and Explanation

### Script Logic

1. **Imports**:
   - `sys`: For command-line arguments.
   - `spotipy` and `SpotifyOAuth`: For interacting with the Spotify API.
   - `youtube_dl`: For extracting information from YouTube music playlists.

2. **Spotify Related Functions**:
   - `get_spotify_tracks(sp, playlist_link)`:
     - Extracts playlist name and tracks from the given Spotify playlist URL.
     - `playlist_link` should be a URL of a Spotify playlist.
   - `normalize_track_name(track_name)`:
     - Normalizes track names for comparison by removing spaces and converting to lowercase.

3. **YouTube Music Related Functions**:
   - `get_youtube_music_tracks(youtube_playlist_url)`:
     - Extracts tracks from the given YouTube playlist URL.
     - `youtube_playlist_url` should be a URL of a YouTube playlist.

4. **File Writing Functions**:
   - `write_tracks_to_file(filename, tracks)`:
     - Writes all tracks to the specified file.
   - `write_unique_tracks_to_file(filename, tracks)`:
     - Writes unique tracks (only in the Spotify playlist and not in the YouTube playlist) to the specified file.

5. **Main Program**:
   - Retrieves Spotify playlist URL and YouTube playlist URL from command-line arguments.
   - Fetches tracks from Spotify and YouTube playlists.
   - Normalizes track names and identifies unique tracks.
   - Writes the results to files.

### Notes

1. **Environment Setup**:
   - Install required Python libraries:
     ```bash
     pip install spotipy youtube_dl
     ```

2. **Getting Spotify API Credentials**:
   - To obtain `CLIENT_ID` and `CLIENT_SECRET` for the Spotify API, refer to this video: [How to Get Spotify API Credentials](https://www.youtube.com/watch?v=mBgg9i1ghNw&t=31s).
   - Ensure your Spotify playlist is set to public for access.

3. **Run your script**:
    - Run the following command, and don't forget to replace `YOUR_SPOTIFY_URL` and `YOUR_YOUTUBE_URL` with your actual playlist URLs:
    ```bash
    python spotify_to_txt.py 'https://open.spotify.com/playlist/YOUR_SPOTIFY_URL' 'https://music.youtube.com/playlist?list=YOUR_YOUTUBE_URL'
    ```

4. **File Paths**:
   - Ensure the script's directory has write permissions for file creation.

5. **Using Third-Party Tools**:
   - You can use [TuneMyMusic](https://www.tunemymusic.com/) for music migration.

### Generated Text Files

- **`<playlist_name>_spotify.txt`**:
  - Contains all tracks extracted from the Spotify playlist, formatted as:
    ```
    1. Track Name - Artist Name
    2. Track Name - Artist Name
    ...
    ```

- **`youtube_music_tracks.txt`**:
  - Contains all tracks extracted from the YouTube Music playlist, formatted as:
    ```
    1. Track Title - Artist Name (if artist is unknown, shown as "Unknown")
    2. Track Title - Artist Name
    ...
    ```

- **`<playlist_name>_unique.txt`**:
  - Contains tracks that are only in the Spotify playlist and not in the YouTube playlist, formatted as:
    ```
    1. Track Name - Artist Name
    2. Track Name - Artist Name
    ...
    ```
