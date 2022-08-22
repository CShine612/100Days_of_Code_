import config
import requests

tmdb_endpoint = "https://api.themoviedb.org/3/search/movie"
# parameters = {"api_key": config.tmbd_api_key,
#               "query": "chef"}
#
#
# response = requests.get(tmdb_endpoint, params=parameters)
# response.raise_for_status()
#
# print(response.json()["results"])


movie_id = "212778"
parameters = {"api_key": config.tmbd_api_key}
response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params=parameters)
response.raise_for_status()

print(response.json())