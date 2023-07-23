
import json

def get_spotify_credentials(file_path):
    try:
        with open(file_path, 'r') as file:
            config_data = json.load(file)

        client_id = config_data.get('clientId')
        client_secret = config_data.get('clientSecret')

        if client_id and client_secret:
            return [client_id, client_secret]
        else:
            print("Error: Client ID and Client Secret not found in the config file.")
            return None
    except Exception as e:
        print(f"Error: Failed to read client config from '{file_path}': {e}")
        return None

if __name__ == "__main__":
    config_file_path = "../config/spotify/config.json"  # Replace this with the actual path to your config file

    credentials = get_spotify_credentials(config_file_path)
