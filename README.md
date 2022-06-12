# spotify-export
Simple tool to export user's Spotify playlists to simple CSV files.

# Requirements
- Create an API key from the [Spotify developers portal](https://developer.spotify.com/) with scopes :
  - playlist-read-private
  - user-read-private
- Use Python 3.6+
- Install Python requirements
`pip install -r requirements.txt`
- Set the following environment variables :
  - `SPOTIPY_CLIENT_ID`
  - `SPOTIPY_CLIENT_SECRET`
  - `SPOTIPY_REDIRECT_URI`

# Usage
`python3 spotify_export.py`
It will create files under `./data` directory with the user's playlists
