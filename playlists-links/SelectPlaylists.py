import json

def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def is_valid_input(answer):
    return answer.lower() in ["y", "n"]

def select_playlists(playlists):
    selected_links = []
    for playlist in playlists:
        print(f"Would you like to download: {playlist['name']}? (Y/N)")
        answer = input().strip().lower()

        while not is_valid_input(answer):
            print("Invalid input. Please enter Y or N.")
            answer = input().strip().lower()

        if answer == "y":
            selected_links.append(playlist['link'])

    return selected_links

if __name__ == "__main__":
    input_filename = "playlists.json"
    output_filename = "selected.json"

    playlists = load_json(input_filename)

    if playlists:
        print("Would you like to download all playlists? (Y/N): ")
        all_playlists_answer = input().strip().lower()

        while not is_valid_input(all_playlists_answer):
            print("Invalid input. Please enter Y or N.")
            all_playlists_answer = input().strip().lower()

        if all_playlists_answer == "y":
            selected_links = [playlist['link'] for playlist in playlists]
        else:
            selected_links = select_playlists(playlists)

        if selected_links:
            save_to_json(selected_links, output_filename)
            print(f"Selected playlist links saved to {output_filename}")
        else:
            # Save an empty list to selected.json if no playlists are selected
            save_to_json([], output_filename)
            print("No playlists were selected.")
    else:
        print("No playlists found in the input file.")
