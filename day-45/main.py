from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
ycwebpage = response.text

soup = BeautifulSoup(ycwebpage,"html.parser")

article_tags = soup.select(".storylink")
score_tags = soup.select(".score")

article_text = []
article_links = []

scores = [int(score.getText().split(" ")[0]) for score in score_tags]
for article in article_tags:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_links.append(link)

max_score = max(scores)
index_max_score = scores.index(max_score)
print(article_text[index_max_score])
print(article_links[index_max_score])
print(max_score)

