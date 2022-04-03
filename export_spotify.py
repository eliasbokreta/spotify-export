from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os
import csv
from datetime import datetime
import re

os.environ['SPOTIPY_CLIENT_ID'] = ""
os.environ['SPOTIPY_CLIENT_SECRET'] = ""
os.environ['SPOTIPY_REDIRECT_URI'] = ""

scope = "playlist-read-private user-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))

current_user = sp.current_user()

username = current_user['id']
results = sp.user_playlists(username)
playlists = results['items']
nbr_playlists = len(playlists)

date = datetime.now().strftime("%Y%m%d")

print(f"Starting fetching {current_user['display_name']}'s {nbr_playlists} playlists...")
while results['next']:
    results = sp.next(results)
    playlists.extend(results['items'])

for playlist in playlists:
    print(f"Exporting playlist {playlist['name']}")
    pattern = "[/'\"_ ]"
    playlist_name = re.sub(pattern, "", playlist['name']).lower()
    with open(f'./data/{playlist_name}_{date}.csv', 'w') as f:
        track_id = 0
        header = ['id', 'artist', 'track', 'album', 'date']
        writer = csv.writer(f)
        writer.writerow(header)
        results = sp.user_playlist_tracks(username, playlist['id'])
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        for item in tracks:
            track = item['track']
            album=sp.album( track['album']['uri'] )
            writer.writerow([
                track_id,
                track['artists'][0]['name'],
                track['name'],
                album['name'],
                album['release_date']
            ])
            track_id += 1
