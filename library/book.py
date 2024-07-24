class Book:

    def __init__(self, book_id: int, title: str, author: str, year: int):
        self.id = book_id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status = "в наличии"
