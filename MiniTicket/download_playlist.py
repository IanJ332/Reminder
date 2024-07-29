import requests
from bs4 import BeautifulSoup

def download_playlist():
    url = "https://music.youtube.com/playlist?list=PLr1Jh9SFeGpv0AsurbRf3TYGJKc3YHkUO&si=NeR9lAWQQcb4Sl0e"

    # Send GET request to the URL and get HTML response
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all songs in the playlist and extract their information
            songs = []
            for song in soup.find_all('div', class_='style-scope ytdusic-searchresult-renderer'):
                title = song.find('a').text.strip()
                artist = song.find('span', class_='style-scope ytdmusic-metadata-renderer')['title']
                duration = song.find('span', class_='style-scope ytdmusic-metadata-renderer')['data-duration']

                # Add the song information to the list
                songs.append({
                    'title': title,
                    'artist': artist,
                    'duration': duration
                })

            # Write the playlist contents to a text file
            with open('playlist.txt', 'w') as f:
                for i, song in enumerate(songs):
                    line = f"{i+1}. {song['title']} by {song['artist']} - {song['duration']}\n"
                    f.write(line)

        else:
            print("Failed to download the playlist")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_playlist()
