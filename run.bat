cd .\playlists-links\ 
python spotify_playlists_to_json.py


for /f "usebackq tokens=*" %%a in (`python -c "import json; urls = json.load(open('playlists.json')); print('\n'.join(urls))"`) do (
    echo Running deemix for: %%a
    deemix "%%a"
)

pause