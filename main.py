#!/usr/bin/env python

import itertools
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'playlist-read-private user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

all_playlists = [tuple([p['id'], p['name']]) for p in sp.current_user_playlists(limit=50)['items']]

for playlist_pair in itertools.combinations(all_playlists, r=2):
    left_playlist_id, left_playlist_name = playlist_pair[0]
    right_playlist_id, right_playlist_name = playlist_pair[1]

    left_playlist_tracks = [t['track']['name'] for t in sp.playlist(left_playlist_id)['tracks']['items']]
    right_playlist_tracks = [t['track']['name'] for t in sp.playlist(right_playlist_id)['tracks']['items']]
    intersection = set(left_playlist_tracks).intersection(set(right_playlist_tracks))

    if intersection:
        print(f'Playlists {left_playlist_name} and {right_playlist_name} have {len(intersection)} songs in common: {intersection}')
