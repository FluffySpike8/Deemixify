from getDownloadPath import get_download_location_from_config
import os
import shutil

def  move_playlist_files():
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

if __name__ == "__main__":
    move_playlist_files()
