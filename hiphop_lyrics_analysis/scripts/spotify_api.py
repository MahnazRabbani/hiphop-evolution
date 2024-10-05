import requests
import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from .env
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Function to get Spotify access token
def get_spotify_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(auth_url, headers=headers, data=data)
    response_data = response.json()
    return response_data['access_token']

# Function to get top rap songs for a given year
def get_top_rap_songs(year, limit=10):
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    search_url = f"https://api.spotify.com/v1/search"
    query = f"year:{year} genre:hip-hop"
    params = {
        "q": query,
        "type": "track",
        "limit": limit
    }
    response = requests.get(search_url, headers=headers, params=params)
    tracks = response.json()['tracks']['items']
    
    songs = []
    for track in tracks:
        song_info = {
            'title': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'spotify_url': track['external_urls']['spotify']
        }
        songs.append(song_info)
    
    return songs

if __name__ == "__main__":
    # Example usage: Get top 10 rap songs from 1990
    top_songs = get_top_rap_songs(1990, limit=10)
    for song in top_songs:
        print(song)
