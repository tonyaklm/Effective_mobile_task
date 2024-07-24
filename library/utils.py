from typing import List, Dict
from library.constants import filename
import json
import os


def open_file() -> List[Dict]:
    """Opens json file and if not exist creates one"""

    if os.path.isfile(filename):
        with open(filename) as books_json:
            return json.load(books_json)
    with open(filename, 'w') as f:
        f.write(json.dumps([], indent=2))
    return []


def write_to_file(books: List[Dict]) -> None:
    """Writes to file list of json"""

    with open(filename, mode='w') as f:
        f.write(json.dumps(books, indent=2))


def find_book(books: List[Dict], book_id: int) -> int:
    """Finds book's index in List by its id and returns -1 if book is not in library"""

    book_index = -1
    for index, book in enumerate(books):
        if book["id"] == book_id:
            book_index = index
            break
    return book_index


def print_books(books: List[Dict]) -> str:
    """Converts list of json books into string"""

    output = []
    for book in books:
        output_of_book = "----------------------\n"
        output_of_book += "Id книги: {}\n".format(book["id"])
        output_of_book += "Название книги: {}\n".format(book["title"])
        output_of_book += "Автор: {}\n".format(book["author"])
        output_of_book += "Год: {}\n".format(book["year"])
        output_of_book += "Статус книги: {}\n".format(book["status"])
        output.append(output_of_book)
    output.append("----------------------\n")
    return "".join(output)
