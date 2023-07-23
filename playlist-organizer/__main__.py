

import os
from movePlaylistFiles import move_playlist_files
from moveArtwork import move_artwork_files
from makeAndroidCompatible import make_android_compatible
from getDownloadPath import get_download_location_from_config

def main():

    try:
        # Execute move_playlist_files() from movePlaylistFiles.py
        print("Executing movePlaylistFiles.py...")
        move_playlist_files()

        # Execute move_artwork_files() from moveArtwork.py
        print("Executing moveArtwork.py...")
        move_artwork_files()

        # Execute make_android_compatible() from makeAndroidCompatible.py
        print("Executing makeAndroidCompatible.py...")
        make_android_compatible()

        print("All scripts executed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
