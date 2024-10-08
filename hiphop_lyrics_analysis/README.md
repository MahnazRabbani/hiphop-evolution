
# HipHop Lyrics Analysis

This project is a part of a **HipHop Evolution** analysis, focusing on gathering and analyzing lyrics from hip-hop songs across different eras. It uses the Genius API to retrieve song lyrics and updates them into a CSV file containing song metadata.

## Project Structure
```
├── hiphop_lyrics_analysis
│   ├── README.md
│   ├── data
│   │   ├── 1995_rap_lyrics.csv
│   │   └── hiphop_eras_songs.csv
│   ├── notebooks
│   │   └── data_prep.ipynb
│   ├── requirements.txt
│   ├── scripts
│   │   ├── collect_lyrics.py
│   │   ├── era_top_songs.py
│   │   ├── genius_api.py
│   │   └── spotify_api.py
│   └── tests
│       └── test_lyrics_script.py
├── requirements.txt
└── venv
```


### Directories and Files

- **`hiphop_lyrics_analysis/data`**: Contains CSV files used for lyrics collection.
    - `1995_rap_lyrics.csv`: Lyrics from rap songs in 1995.
    - `hiphop_eras_songs.csv`: Main dataset containing hip-hop songs and associated metadata (Title, Artist, Year, Era).
    
- **`hiphop_lyrics_analysis/notebooks`**: Contains Jupyter notebooks for data exploration and preparation.
    - `data_prep.ipynb`: Data preparation steps for lyrics analysis.
    
- **`hiphop_lyrics_analysis/scripts`**: Contains scripts for fetching data and interacting with APIs.
    - `collect_lyrics.py`: Script to update a CSV file by fetching lyrics from the Genius API.
    - `genius_api.py`: Functions to interact with the Genius API to search for songs and retrieve lyrics.
    - `era_top_songs.py`: handles fetching top songs (hard-coded initially) from different eras.
    - `spotify_api.py`: interacts with the Spotify API for song metadata. [not used at the end]
    
- **`hiphop_lyrics_analysis/tests`**: Contains unit tests to verify the functionality of the project.
    - `test_lyrics_script.py`: Unit tests for the lyrics collection script.

## Getting Started

### Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.x**: The project requires Python 3 to run.
- **Virtual environment** (recommended): Set up a virtual environment for dependency management.

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/MahnazRabbani/hiphop-evolution
   ```

2. Navigate to the project directory:
   ```bash
   cd hiphop-lyrics-analysis
   ```

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the `.env` file with your Genius API key:
   - Create a file named `.env` in the `scripts` directory with the following content:
     ```
     GENIUS_API_KEY=your_genius_api_key
     ```
   You can get your Genius API key by signing up at [Genius](https://genius.com/).

### Running the Lyrics Collection Script

To update the CSV file with song lyrics:

```bash
python hiphop_lyrics_analysis/scripts/collect_lyrics.py
```

This script fetches lyrics from the Genius API for each song in the `hiphop_eras_songs.csv` file and adds them to the file under a new "Lyrics" column. If lyrics are not found for a particular song, the script will print an error message.

### Running Unit Tests

To verify the functionality of the project, you can run the provided unit tests:

```bash
python -m unittest discover hiphop_lyrics_analysis/tests
```

The tests are located in `test_lyrics_script.py` and are designed to validate the functionality of the `collect_lyrics.py` script.

## Scripts Overview

### `collect_lyrics.py`

This script reads a CSV file containing song metadata (Title, Artist, Year, Era) and uses the Genius API to fetch lyrics for each song. The fetched lyrics are then written back to the CSV file.

Key function:

- `update_csv_with_lyrics(csv_file)`: Reads the CSV file, fetches lyrics using the Genius API, and updates the file with the retrieved lyrics.

### `genius_api.py`

This script contains helper functions to interact with the Genius API.

Key functions:

- `search_song_on_genius(title, artist)`: Searches for a song on Genius by its title and artist.
- `get_lyrics_from_genius_url(song_url)`: Retrieves the lyrics from a Genius song URL.

## Requirements

The project's dependencies are listed in `requirements.txt`:

- `requests`: Used for making HTTP requests to the Genius API.
- `beautifulsoup4`: Used for parsing HTML to scrape lyrics from the Genius webpage.
- `python-dotenv`: For loading environment variables from the `.env` file.
- Other dependencies needed for Jupyter notebooks and testing (e.g., pandas, unittest).

You can install these dependencies using:

```bash
pip install -r requirements.txt
```

## License



## Acknowledgments

- Lyrics data powered by [Genius API](https://genius.com/).
- Python libraries such as `requests`, `BeautifulSoup`, and `pandas` used for data retrieval and processing.