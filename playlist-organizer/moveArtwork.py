
from getDownloadPath import get_download_location_from_config
import os
import shutil

def move_artwork_files():
    download_location = get_download_location_from_config()

    if download_location:
        artwork_folder = os.path.join(download_location, "..", "Playlist", "Artwork")

        if not os.path.exists(artwork_folder):
            try:
                os.makedirs(artwork_folder)
                print(f"Created Artwork folder at: {artwork_folder}")
            except Exception as e:
                print(f"Error: Failed to create Artwork folder: {e}")
                return

        jpg_files = [file for file in os.listdir(download_location) if file.lower().endswith(".jpg")]

        if jpg_files:
            for jpg_file in jpg_files:
                src_path = os.path.join(download_location, jpg_file)
                dest_path = os.path.join(artwork_folder, jpg_file)
                try:
                    shutil.move(src_path, dest_path)
                    print(f"Moved '{jpg_file}' to: {dest_path}")
                except Exception as e:
                    print(f"Error: Failed to move '{jpg_file}': {e}")
        else:
            print("No .jpg files found in the source folder.")

if __name__ == "__main__":
    move_artwork_files()
