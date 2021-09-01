# Spoty
A script for searching duplicates in your playlists

## Settings
You need to create an application in your spotify account dashboard, copy client id, client secret and set redirect uri. Then set three corresponding environment variables in order to run this script: `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET` and `SPOTIPY_REDIRECT_URI`. Example is in .env.example.

## Info
When running this script for the first time, you need to authenticate and accept access to your playlists in browser. Then paste the link in address bar to script promt.

## Run
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
source .env
chmod u+x main.py
```
