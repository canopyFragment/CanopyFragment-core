class Article:
    def __init__(self, website, title, author, date, url):
        self.website = website
        self.title = title
        self.author = author
        self.date = date
        self.url = url

    def __repr__(self):
        print(f"Article({self.website}, {self.title}, {self.author}, {self.date})")

    def __str__(self):
        return f"{self.title} - {self.author} - {self.date}"

    def to_json(self):
        return {
            "website": self.website.to_json(),
            "title": self.title,
            "author": self.author,
            "date": self.date,
            "url": self.url
        }
