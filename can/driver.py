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


class Zero1Net(Website):
    def __init__(self):
        self.name = "01net"
        self.url = "https://www.01net.com/actualites/"
        self.category = "tech"

    def fetch_last_article(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the first section tag and the direct main tag inside
        section = soup.find("section")
        main = section.find("main")

        # Inside the main, fetch the href from the first link
        link = main.find("a")
        url = link.get("href")

        # Inside this link, fetch the first div and get the text only
        div = link.find("div")
        title = div.text

        return Article(
            self,
            title,
            "NaN",
            datetime.now().date(),
            url,
        )


class GenerationNT(Website):
    def __init__(self):
        self.name = "generation-nt"
        self.url = "https://www.generation-nt.com/actualites"
        self.category = "tech"

    def fetch_last_article(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the div that have for id "body-content"
        body = soup.find("div", id="body-content")

        # Find the first article tag that is inside the second section of the page
        section = body.find_all("section")[1]
        article = section.find("article")

        # Fetch the first link inside the article and get the href and the text
        link = article.find_all("a")[1]
        url = link.get("href")
        title = link.text

        # The link is relative, so we need to add the base url
        article_link = url.split("/")[-1]
        url = f"{self.url}/{article_link}"
        
        return Article(
            self,
            title,
            "NaN",
            datetime.now().date(),
            url,
        )
        

class LesNumeriques(Website):
    def __init__(self):
        self.name = "lesnumeriques"
        self.url = "https://www.lesnumeriques.com/"
        self.category = "tech"

    def fetch_last_article(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the first section, then the div with id="hot-news"
        section = soup.find("section")
        div = section.find("div", id="hot-news")

        # Inside this div, with fetch the first line of the list 
        ul = div.find_all("ul")[1]
        li = ul.find("li")
        article = li.find("article")

        url = article.find("a").get("href")
        title = article.find("h3").text

        article_link = url.split("/")[-1]
        url = f"{self.url}/{article_link}"

        return Article(
            self,
            title,
            "NaN",
            datetime.now().date(),
            url,
        )


class Developpez(Website):
    def __init__(self):
        self.name = "developpez"
        self.url = "https://www.developpez.com/"
        self.category = "tech"

    def fetch_last_article(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the first div with the class "colonneActu"
        div = soup.find("div", class_="colonneActu")

        # Find the first article inside that div
        article = div.find("article")

        # Find the first link
        link = article.find("a")
        url = link.get("href")
        title = link.text

        article_link = url
        url = f"{self.url}/{article_link}"

        return Article(
            self,
            title,
            "NaN",
            datetime.now().date(),
            url,
        )


class Clubic(Website):
    def __init__(self):
        self.name = "clubic"
        self.url = "https://www.clubic.com/"
        self.category = "tech"

    def fetch_last_article(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Get the div with the id "infos-flux-home"
        div = soup.find("div", id="infos-flux-home")

        # Get the first div with the class "posts"
        posts = div.find("div", class_="posts")

        # Get the first link
        link = posts.find("a")
        url = link.get("href")
        title = link.text

        article_link = url
        url = f"{self.url}/{article_link}"

        return Article(
            self,
            title,
            "NaN",
            datetime.now().date(),
            url,
        )




def driver_factory(driver_name: str):
    mapper = dict(
        korben=Korben,
        zero1net=Zero1Net,
        generation_nt=GenerationNT,
        lesnumeriques=LesNumeriques,
        developpez=Developpez,
        clubic=Clubic,
    )

    return mapper[driver_name]()


if __name__ == "__main__":
    website = driver_factory("developpez")
    art = website.fetch_last_article()
    print(art)
    print(art.url)
