import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)

movies_page = response.text


soup = BeautifulSoup(movies_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")


title_list = [titles[i].get_text() for i in range(len(titles) - 1, -1, -1)]

movie_string = "\n".join(title_list)


with open("movies.txt", "w") as file:
    file.write(movie_string)
