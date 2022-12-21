from datetime import datetime

import requests
from bs4 import BeautifulSoup

from can.core.websites import Website
from can.core.articles import Article


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

        # Find the first link after the title and fetch the href from it
        link = h2.find_next("a")
        url = link.get("href")

        return Article(
            self,
            h2.text,
            "Korben",
            datetime.now().date(),
            url,
        )


def driver_factory(driver_name: str):
    mapper = dict(
        korben=Korben,
    )

    return mapper[driver_name]()


if __name__ == "__main__":
    korben = Korben()
    art = korben.fetch_last_article()
    print(art)
    print(art.url)
