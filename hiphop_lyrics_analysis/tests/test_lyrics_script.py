import unittest
from unittest.mock import patch
import pandas as pd
import os

# Import the function to be tested from collect_lyrics.py
from hiphop_lyrics_analysis.scripts.collect_lyrics import update_csv_with_lyrics

class TestLyricsScript(unittest.TestCase):

    def setUp(self):
        # Create a temporary CSV file for testing
        self.test_csv = 'test_hiphop_eras_songs.csv'
        data = {
            'Song Title': ['Song A', 'Song B'],
            'Artist': ['Artist A', 'Artist B'],
            'Year': [2000, 2010],
            'Era': ['2000s', '2010s']
        }
        self.df = pd.DataFrame(data)
        self.df.to_csv(self.test_csv, index=False)
    
    def tearDown(self):
        # Remove the temporary test CSV file after tests
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    @patch('hiphop_lyrics_analysis.scripts.genius_api.search_song_on_genius')
    @patch('hiphop_lyrics_analysis.scripts.genius_api.get_lyrics_from_genius_url')
    def test_update_csv_with_lyrics(self, mock_get_lyrics, mock_search_song):
        # Mock the search_song_on_genius to return a simulated response
        mock_search_song.side_effect = [
            {'url': 'https://genius.com/Song-A-lyrics'},
            {'url': 'https://genius.com/Song-B-lyrics'}
        ]
        
        # Mock the get_lyrics_from_genius_url to return dummy lyrics
        mock_get_lyrics.side_effect = [
            'These are the lyrics for Song A',
            'These are the lyrics for Song B'
        ]

        # Run the function to update the CSV file
        update_csv_with_lyrics(self.test_csv)

        # Read the CSV file to check if the lyrics were added correctly
        updated_df = pd.read_csv(self.test_csv)

        # Check if the 'Lyrics' column is correctly populated
        self.assertIn('Lyrics', updated_df.columns)
        self.assertEqual(updated_df['Lyrics'][0], 'These are the lyrics for Song A')
        self.assertEqual(updated_df['Lyrics'][1], 'These are the lyrics for Song B')

    @patch('hiphop_lyrics_analysis.scripts.genius_api.search_song_on_genius')
    @patch('hiphop_lyrics_analysis.scripts.genius_api.get_lyrics_from_genius_url')
    def test_lyrics_not_found(self, mock_get_lyrics, mock_search_song):
        # Mock the search_song_on_genius to return None when song is not found
        mock_search_song.side_effect = [None, None]
        
        # Mock the get_lyrics_from_genius_url (won't be called in this case)
        mock_get_lyrics.side_effect = [None, None]

        # Run the function to update the CSV file
        update_csv_with_lyrics(self.test_csv)

        # Read the CSV file to check if the lyrics were handled correctly
        updated_df = pd.read_csv(self.test_csv)

        # Check that the Lyrics column is empty when no song is found
        self.assertIn('Lyrics', updated_df.columns)
        self.assertTrue(pd.isna(updated_df['Lyrics'][0]))
        self.assertTrue(pd.isna(updated_df['Lyrics'][1]))

if __name__ == '__main__':
    unittest.main()
