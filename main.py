import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())
data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])
#print(json.dumps(data,indent=4))#prints all data
# print(soup.prettify())

def find_articles(data):
    if isinstance(data, dict):
        for k, v in data.items():
            if k.startswith("ImageMeta:"):
                yield v["titleText"]
            else:
                yield from find_articles(v)
    elif isinstance(data, list):
        for i in data:
            yield from find_articles(i)
with open("movies.txt", mode="w") as file:
    for a in find_articles(data):
        print(a)
        file.write(f"{a}\n")



# all_movies = soup.find_all(name="h3")
# print(all_movies)
# movie_titles = [movie.getText() for movie in all_movies]
# print(movie_titles[::-1])