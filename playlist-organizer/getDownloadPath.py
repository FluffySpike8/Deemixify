import os
import json

def get_download_location_from_config():
    # Assuming the script is in the same directory as the config.json file
    config_path = "../config/config.json"

    # Check if the config file exists
    if not os.path.exists(config_path):
        print(f"Error: Config file not found at '{config_path}'")
        return None

    try:
        # Read the JSON data from the config file
        with open(config_path, 'r') as file:
            config_data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON data from '{config_path}': {e}")
        return None

    # Get the value of downloadLocation from the config
    download_location = config_data.get('downloadLocation')

    if download_location is None:
        print("Error: 'downloadLocation' key not found in the config file.")
        return None

    # Normalize the path to handle any inconsistencies in the JSON data
    download_location = os.path.normpath(download_location)

    # Check if the downloadLocation is a valid directory
    if not os.path.isdir(download_location):
        print(f"Error: 'downloadLocation' is not a valid directory: '{download_location}'")
        return None

    return download_location

if __name__ == "__main__":
    download_location = get_download_location_from_config()
    if download_location:
        print(f"The download location is: {download_location}")
