from bs4 import BeautifulSoup
import requests
import re
import json

response = requests.get("https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512")
soup = BeautifulSoup(response.text,"html.parser")

movies=soup.find_all('h1',class_="list-item__title")

with open('movie_list.txt','a+') as f:
    for movie in movies[::-1]:
        rank = len(movies) - movies.index(movie)
        title = movie.getText()
        f.write(f"{rank} - {title}\n")