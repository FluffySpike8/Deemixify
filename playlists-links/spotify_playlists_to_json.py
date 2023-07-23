import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from getSpotifyApiCredentials import get_spotify_credentials

# Set your Spotify credentials
os.environ["SPOTIPY_CLIENT_ID"] = get_spotify_credentials("../config/spotify/config.json")[0]
os.environ["SPOTIPY_CLIENT_SECRET"] = get_spotify_credentials("../config/spotify/config.json")[1]
os.environ["SPOTIPY_REDIRECT_URI"] = "https://example.com"

def get_spotify_playlist_links():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-read-private"))

    # Get the user's playlists
    playlists = sp.current_user_playlists()

    playlist_links = []

    for playlist in playlists["items"]:
        playlist_link = playlist["external_urls"]["spotify"]
        playlist_links.append(playlist_link)

    return playlist_links

def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    playlist_links = get_spotify_playlist_links()

    if playlist_links:
        output_filename = "playlists.json"
        save_to_json(playlist_links, output_filename)
        print(f"Playlist links saved to {output_filename}")
    else:
        print("No playlists found.")