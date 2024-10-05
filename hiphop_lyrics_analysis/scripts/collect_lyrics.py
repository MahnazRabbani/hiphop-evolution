import pandas as pd
from spotify_api import get_top_rap_songs
from genius_api import search_song_on_genius, get_lyrics_from_genius_url

# Function to collect lyrics for top songs of a given year
def collect_lyrics_for_year(year, limit=10):
    # Get top songs from Spotify
    top_songs = get_top_rap_songs(year, limit)
    
    song_lyrics = []
    for song in top_songs:
        print(f"Searching lyrics for: {song['title']} by {song['artist']}")
        
        # Search for the song on Genius
        song_info = search_song_on_genius(song['title'], song['artist'])
        if song_info:
            lyrics = get_lyrics_from_genius_url(song_info['url'])
            song['lyrics'] = lyrics if lyrics else "Lyrics not found"
        else:
            song['lyrics'] = "Lyrics not found"
        
        song_lyrics.append(song)
    
    # Convert to DataFrame
    df = pd.DataFrame(song_lyrics)
    return df

if __name__ == "__main__":
    # Example usage: Collect lyrics for top songs from 1995
    lyrics_df = collect_lyrics_for_year(1995, limit=5)
    # Save the data to a CSV file
    lyrics_df.to_csv("hiphop_lyrics_analysis/data/1995_rap_lyrics.csv", index=False)
    print("Lyrics collected and saved successfully.")
