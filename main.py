#!/usr/bin/env python

import itertools
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'playlist-read-private user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlists_tracks = [
        dict(
            id=p['id'],
            name=p['name'],
            tracks=list(map(lambda x: x['track']['name'], sp.playlist(p['id'])['tracks']['items']))
        )
        for p in sp.current_user_playlists(limit=50)['items']
        ]

playlists = map(lambda pt: pt['id'], playlists_tracks)

def find_tracks_by_playlist_id(playlist_id):
    for pt in playlists_tracks:
        if pt['id'] == playlist_id:
            return pt['tracks']

def find_name_by_playlist_id(playlist_id):
    for pt in playlists_tracks:
        if pt['id'] == playlist_id:
            return pt['name']

for playlist_tuple in itertools.combinations(playlists, r=2):
    left_playlist_id = playlist_tuple[0]
    right_playlist_id = playlist_tuple[1]

    left_playlist_tracks = find_tracks_by_playlist_id(left_playlist_id)
    right_playlist_tracks = find_tracks_by_playlist_id(right_playlist_id)

    intersection = set(left_playlist_tracks).intersection(set(right_playlist_tracks))

    if intersection:
        left_playlist_name = find_name_by_playlist_id(left_playlist_id)
        right_playlist_name = find_name_by_playlist_id(right_playlist_id)
        print(f'Playlists {left_playlist_name} and {right_playlist_name} have {len(intersection)} songs in common: {intersection}')
