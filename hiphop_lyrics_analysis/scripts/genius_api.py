import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Genius API token from environment variables
GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")

# Function to search for a song on Genius
def search_song_on_genius(title, artist):
    base_url = "https://api.genius.com"
    headers = {
        "Authorization": f"Bearer {GENIUS_API_KEY}"
    }
    search_url = f"{base_url}/search"
    data = {'q': f"{title} {artist}"}
    response = requests.get(search_url, headers=headers, params=data)

    if response.status_code == 200:
        json_response = response.json()

        # Check if there are any hits
        if 'response' in json_response and json_response['response']['hits']:
            song_info = None
            for hit in json_response['response']['hits']:
                if artist.lower() in hit['result']['primary_artist']['name'].lower():
                    song_info = hit['result']
                    break
            return song_info if song_info else None
        else:
            return None
    else:
        print(f"Error {response.status_code}: {response.json()['meta']['message']}")
        return None

# Function to get lyrics from the Genius URL
def get_lyrics_from_genius_url(song_url):
    # Send a request to the song's URL
    response = requests.get(song_url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all lyrics container divs (multiple sections with data-lyrics-container="true")
    lyrics_containers = soup.find_all('div', {'data-lyrics-container': 'true'})
    
    if not lyrics_containers:
        print("Lyrics containers not found.")
        return None
    
    # Initialize an empty list to store the lyrics
    lyrics = []
    
    # Loop through all the containers and extract text
    for container in lyrics_containers:
        for element in container.children:
            if isinstance(element, str):
                lyrics.append(element.strip())
            elif element.name == 'br':
                # Handle line breaks
                lyrics.append("\n")
            elif element.name == 'a':
                # Handle links (annotated lyrics)
                lyrics.append(element.get_text())
            elif element.name == 'span':
                # Handle spans for annotation highlighting
                lyrics.append(element.get_text())
    
    # Join the lyrics list into a single string
    lyrics_text = "".join(lyrics).strip()
    
    return lyrics_text

# Example usage:
if __name__ == "__main__":
    song_info = search_song_on_genius("Nuthin' But a G Thang", "Dr. Dre")
    if song_info:
        print(f"Found song: {song_info['full_title']}")
        lyrics = get_lyrics_from_genius_url(song_info['url'])
        if lyrics:
            print("Lyrics successfully retrieved!")
            print(lyrics)
        else:
            print("Failed to retrieve lyrics.")
    else:
        print("Song not found on Genius.")
