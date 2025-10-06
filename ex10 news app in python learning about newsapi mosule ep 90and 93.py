import requests
import json

query=input("what type of news are you intrested in?:")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-09-15&sortBy=publishedAt&apiKey=ffe98da6350242b8b52f56e0148aad58"
r=requests.get(url)
news=json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------")
