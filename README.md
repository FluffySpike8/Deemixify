# Deemixify

Tool to fetch a users Spotify playlists and dowload them using deemix.

## Before running

- Make sure that deemix is installed through pip:  
  `pip install deemix`

- Configure deemix (I suggest using deemix-gui for this)  
  The config files should be located in `%appdata%\deemix`  
  This is where you will configure the download path and quality also arl will be set here and spotify `cliendID` and `cliendSecret` for deemix.

- Configure spotify api
  1.  Make an application on https://developer.spotify.com/
  2.  Add `cliendID` and `cliendSecret` to `spotify-credentials.json`

## Running the program

To run the program, just double click run.bat. The music files will be downloaded to the path you chose.
