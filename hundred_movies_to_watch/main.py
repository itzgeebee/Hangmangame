# A simple webscraping using beautiful soup applied in scraping the 100 greatest movies and making a .txt files
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL).text
soup = BeautifulSoup(response, "html.parser")
movies = soup.find_all(name="h3", class_="title")
all_movies = [movie.get_text() for movie in movies]

ordered_movies = all_movies[::-1]
print(ordered_movies)
with open("100_greatest_movies.txt", "w") as great_movies:
    for i in ordered_movies:
        great_movies.write(f"{i}\n")

