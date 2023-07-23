
from getDownloadPath import get_download_location_from_config
import os
import shutil

def make_android_compatible():
    download_location = get_download_location_from_config()

    if download_location:
        m3u8_folder = os.path.join(download_location, "..", "Playlist", "m3u8")

        if not os.path.exists(m3u8_folder):
            print("Error: m3u8 folder not found in the source directory.")
            return

        android_folder = os.path.join(download_location, "..", "Playlist", "Android")

        if not os.path.exists(android_folder):
            try:
                os.makedirs(android_folder)
                print(f"Created Android folder at: {android_folder}")
            except Exception as e:
                print(f"Error: Failed to create Android folder: {e}")
                return

        m3u8_files = [file for file in os.listdir(m3u8_folder) if file.lower().endswith(".m3u8")]

        if m3u8_files:
            for m3u8_file in m3u8_files:
                src_path = os.path.join(m3u8_folder, m3u8_file)
                dest_path = os.path.join(android_folder, os.path.splitext(m3u8_file)[0] + ".m3u")

                try:
                    shutil.copy(src_path, dest_path)
                    print(f"Copied '{m3u8_file}' to: {dest_path}")
                except Exception as e:
                    print(f"Error: Failed to copy '{m3u8_file}': {e}")
        else:
            print("No .m3u8 files found in the source folder.")

if __name__ == "__main__":
    make_android_compatible()
