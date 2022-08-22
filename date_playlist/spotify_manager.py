import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

class SpotifyManager:

    def __init__(self):
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.spotify_client_id,
                                               client_secret=config.spotify_clien_secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))

            self.user = self.sp.current_user()["id"]
            self.playlists = {}

    def song_search(self, songs, year):
        song_ids = []
        for song in songs:
            result = self.sp.search(q=f"track: {song} year: {year}")["tracks"]["items"]
            if len(result) == 0:
                pass
            else:
                song_ids.append(result[0]["id"])
        return song_ids

    def create_playlist(self, date):
        if date in self.playlists.keys():
            pass
        else:
            self.playlists[date] = self.sp.user_playlist_create(self.user, f"{date} Billboard Top100", public=False)["id"]

    def add_songs(self, songs, date):
        song_ids = self.song_search(songs, date[:4])
        self.sp.playlist_add_items(self.playlists[date], song_ids)


