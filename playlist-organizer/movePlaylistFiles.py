from getDownloadPath import get_download_location_from_config
import os
import shutil
from os.path import join as path_join


def move_playlist_files():
    download_location = get_download_location_from_config()

    if download_location:
        m3u8_folder = os.path.join(download_location, "..", "Playlist", "m3u8")

        if not os.path.exists(m3u8_folder):
            try:
                os.makedirs(m3u8_folder)
                print(f"Created m3u8 folder at: {m3u8_folder}")
            except Exception as e:
                print(f"Error: Failed to create m3u8 folder: {e}")
                return

        m3u8_files = [file for file in os.listdir(download_location) if file.lower().endswith(".m3u8")]

        if m3u8_files:
            for m3u8_file in m3u8_files:
                src_path = os.path.join(download_location, m3u8_file)
                dest_path = os.path.join(m3u8_folder, m3u8_file)

                try:
                    shutil.move(src_path, dest_path)
                    print(f"Moved '{m3u8_file}' to: {dest_path}")
                    
                    # Modify the content of the .m3u8 file
                    with open(dest_path, 'r') as file:
                        lines = file.readlines()

                    with open(dest_path, 'w') as file:
                        for line in lines:
                            # Remove empty lines and replace backslashes with forward slashes
                            line = line.strip().replace('\\', '/')

                            # Add ../../ and the end of the download path
                            if line:
                                modified_line = f"../../{os.path.basename(download_location)}/{line}\n"
                                file.write(modified_line)

                    print(f"Modified paths in '{m3u8_file}'")
                except Exception as e:
                    print(f"Error: Failed to move or modify '{m3u8_file}': {e}")
        else:
            print("No .m3u8 files found in the source folder.")

def add_external_music_files_to_playlist():
    download_location = get_download_location_from_config()

    favorites_m3u8_path = os.path.join(download_location, "..", "Playlist", "m3u8", "Favorites.m3u8")
    
    if os.path.exists(favorites_m3u8_path):
        print("Adding external music files to playlist...")
        external_folder = os.path.join(download_location, "External")
        music_files = []

        # Recursively find all music files in External folder
        for root, _, files in os.walk(external_folder):
            for file in files:
                if file.lower().endswith((".mp3", ".wav", ".flac")):
                    file_path = os.path.relpath(os.path.join(root, file), external_folder)
                    music_files.append(file_path.replace('\\', '/'))

        # Add music files from download_location/External to the playlist file
        with open(favorites_m3u8_path, 'a') as file:
            for music_file in music_files:
                file.write(f"../../{os.path.basename(download_location)}/External/{music_file}\n")

        print(f"Added music files to 'Favorites.m3u8'")

if __name__ == "__main__":
    move_playlist_files()
    add_external_music_files_to_playlist()