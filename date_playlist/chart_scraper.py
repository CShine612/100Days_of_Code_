import requests
from bs4 import BeautifulSoup


class SongFinder:

    def __init__(self, year):
        self.url = f"https://www.billboard.com/charts/hot-100/{year}"

    def get_list(self):
        response = requests.get(self.url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        list_items = soup.find_all(name="li", class_="o-chart-results-list__item")
        songs = []
        for item in list_items:
            if item.find(name="h3"):
                songs.append(item.find(name="h3").getText().strip())
        return songs
