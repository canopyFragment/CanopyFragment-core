class Website:
    def __init__(self, name, url, category):
        self.name = name
        self.url = url
        self.category = category

    def __repr__(self):
        print(f"Website({self.name}, {self.url}, {self.category})")

    def __str__(self):
        return f"{self.name} - {self.url} - {self.category}"

    def to_json(self):
        return {
            "name": self.name,
            "url": self.url,
            "category": self.category
        }

    def fetch_last_article(self):
        raise NotImplementedError
