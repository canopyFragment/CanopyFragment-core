from datetime import datetime

import requests
from bs4 import BeautifulSoup

from core.websites import Website
from core.articles import Article


class Korben(Website):
    def __init__(self):
        self.name = "Korben"
        self.url = "https://korben.info"
        self.category = "tech"

    def fetch_last_article(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        article = soup.find("article")
        h2 = article.find("h2")

        return Article(
            self,
            h2.text,
            "Korben",
            datetime.now().date()
        )


if __name__ == "__main__":
    korben = Korben()
    print(korben.fetch_last_article())