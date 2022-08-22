from bs4 import BeautifulSoup
import requests

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# print(soup.title.string)

response = requests.get("https://news.ycombinator.com/")

html = response.text

soup = BeautifulSoup(html, "html.parser")

article_tags = soup.find_all(name="a", class_="titlelink")


texts = [item.getText() for item in article_tags]

links = [item.get("href") for item in article_tags]

upvotes = [int(item.getText().split()[0]) for item in soup.find_all(name="span", class_="score")]

index = 0
highest_votes = 0

for ind, item in enumerate(upvotes):
    if item > highest_votes:
        index = ind
        highest_votes = item


highest_votes_data = (texts[index], links[index], upvotes[index])

print(highest_votes_data)
