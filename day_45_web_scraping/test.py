# import lxml
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")

yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")


article_texts = [
    tag.get_text() for tag in soup.find_all(name="span", class_="titleline")
]

article_links = [
    tag.find("a").get("href") for tag in soup.find_all(name="span", class_="titleline")
]


article_upvotes = [
    int(tag.get_text().split()[0]) for tag in soup.find_all(name="span", class_="score")
]


max_votes = 0
index = 0
for i, vote in enumerate(article_upvotes):
    if max_votes < vote:
        max_votes = vote
        index = i

print(
    f"The top article is {article_texts[index]}, link: {article_links[index]}, with {article_upvotes[index]} upvotes!"
)
