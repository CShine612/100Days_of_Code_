import re
from chart_scraper import SongFinder
from spotify_manager import SpotifyManager

valid_input = r"[2][0][012][0-9]-(0[1-9]|1[012])-([0-2][0-9]|3[01])"

while True:
    date = input("Please enter a date in the last 20 years in YYYY-MM-DD format: ")
    if re.fullmatch(valid_input, date):
        break

date_songs = SongFinder(date)
songs = date_songs.get_list()
spoty = SpotifyManager()

spoty.create_playlist(date)
spoty.add_songs(songs, date)