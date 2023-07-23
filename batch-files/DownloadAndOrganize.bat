cd ..

cd .\playlists-links\ 
python spotify_playlists_to_json.py

cd ..

for /f "usebackq tokens=*" %%a in (`python -c "import json; urls = json.load(open('.\playlists-links\playlists.json')); print('\n'.join(urls))"`) do (
    echo Running deemix for: %%a
    deemix --portable "%%a"
)


cd .\playlist-organizer
python __main__.py

pause