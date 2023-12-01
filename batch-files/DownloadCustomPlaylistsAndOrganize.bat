cd ..

for /f "usebackq tokens=*" %%a in (`python -c "import json; urls = json.load(open('custom_playlists.json')); print('\n'.join(urls))"`) do (
    echo Running deemix for: %%a
    deemix --portable "%%a"
)


cd .\playlist-organizer
python __main__.py

pause