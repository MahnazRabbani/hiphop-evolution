import pandas as pd
from time import sleep
import os
#from spotify_api import get_top_rap_songs
from hiphop_lyrics_analysis.scripts.genius_api import search_song_on_genius, get_lyrics_from_genius_url

# Function to update the CSV file with song lyrics
def update_csv_with_lyrics(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Check if the 'Lyrics' column already exists, if not, create one
    if 'Lyrics' not in df.columns:
        df['Lyrics'] = None

    # Iterate over each row (song)
    for idx, row in df.iterrows():
        song_title = row['Song Title']
        artist = row['Artist']
        year = row['Year']
        era = row['Era']
        
        print(f"Fetching lyrics for: {song_title} by {artist}")
        
        # Search for the song on Genius
        song_info = search_song_on_genius(song_title, artist)
        
        if song_info:
            song_url = song_info['url']  # Genius URL for the song
            
            # Get the lyrics from the song's Genius URL
            lyrics = get_lyrics_from_genius_url(song_url)
            
            if lyrics:
                # Update the 'Lyrics' column with the fetched lyrics
                df.at[idx, 'Lyrics'] = lyrics
            else:
                print(f"Lyrics not found for: {song_title} by {artist}")
        else:
            print(f"Song not found on Genius: {song_title} by {artist}")

        # To avoid being rate-limited, add a delay between API requests
        sleep(2)  # Adjust this value based on API limits

    # Save the updated DataFrame back to a CSV file
    df.to_csv(csv_file, index=False)
    print(f"CSV file updated with lyrics: {csv_file}")

# Update the CSV file
current_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(current_dir, '../data/hiphop_eras_songs.csv')
update_csv_with_lyrics(csv_file_path)
