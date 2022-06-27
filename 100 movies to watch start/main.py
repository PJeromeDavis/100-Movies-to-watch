import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
tags = soup.find_all(name="h3", class_="title")
movie_list = []
for tag in tags:
    string = tag.getText()
    movie_list.append(string)

movie_list.reverse()
with open("movies.txt", mode="w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
