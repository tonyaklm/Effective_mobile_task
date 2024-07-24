from library.book import Book
from library.utils import write_to_file, find_book, open_file, print_books
from datetime import datetime


class BookRepository:

    def __init__(self):
        pass

    def get(self) -> str:
        """Get all existing books in library"""

        return print_books(open_file())

    def get_by(self, search_key: str, search_value: str) -> (str, bool):
        """Get books that have specific key = author/year/title"""

        suitable = []
        if search_key == "year":
            try:
                search_value = int(search_value)
            except ValueError:
                return "Неверный год", True

            if search_value < 1457 or search_value > datetime.now().year:
                return "Год должен быть в диапазоне от 1457 до {}".format(datetime.now().year), True

        json_decoded = open_file()

        for book in json_decoded:
            book_value = book.get(search_key, None)
            if search_key != "year":
                if search_value.lower() in book_value.lower():
                    suitable.append(book)
            elif search_value == book_value:
                suitable.append(book)
        return print_books(suitable), False

    def add(self, title: str, author: str, year: str) -> (str, bool):
        """Add new book with specific title, author, year and unique id"""

        new_id = 1
        books = open_file()
        if books:
            new_id = books[-1]["id"] + 1

        try:
            year = int(year)
        except ValueError:
            return "Неверный год", 3

        if year < 1457 or year > datetime.now().year:
            return "Год должен быть в диапазоне от 1457 до {}".format(datetime.now().year), True

        new_book = Book(new_id, title, author, year)

        json_decoded = open_file()

        json_decoded.append(new_book.__dict__)

        write_to_file(json_decoded)
        output_massage = "----------------------\n" \
                         "Id: {}\n" \
                         "Название: {}\n" \
                         "Автор: {}\n" \
                         "Год: {}\n" \
                         "Статус: {}\n" \
                         "Книга успешно добавлена\n" \
                         "----------------------".format(new_book.id, new_book.title, new_book.author, new_book.year,
                                                         new_book.status)
        return output_massage, False

    def delete(self, book_id: str) -> (str, bool):
        """Delete a book by its id"""

        try:
            book_id = int(book_id)
        except ValueError:
            return "Неверный id", True

        books = open_file()

        book_index = find_book(books, book_id)
        if book_index == -1:
            return "Несуществующий id", True
        deleted_book = books[book_index]

        books.pop(book_index)

        write_to_file(books)

        output_massage = "----------------------\n" \
                         "Id: {}\n" \
                         "Название: {}\n" \
                         "Автор: {}\n" \
                         "Год: {}\n" \
                         "Статус: {}\n" \
                         "Книга успешно удалена\n" \
                         "----------------------".format(deleted_book['id'], deleted_book['title'],
                                                         deleted_book['author'], deleted_book['year'],
                                                         deleted_book['status'])
        return output_massage, False

    def update(self, book_id: str, new_status: str) -> (str, int):
        """Change status for a book by its id"""

        if new_status not in ["в наличии", "выдана"]:
            return "Недопустимый статус", 1

        try:
            book_id = int(book_id)
        except ValueError:
            return "Неверный id", 2

        books = open_file()

        book_index = find_book(books, book_id)
        if book_index == -1:
            return "Несуществующий id", 2

        books[book_index]["status"] = new_status

        write_to_file(books)

        output_message = "Статус книги '{}' успешно изменен на '{}'".format(books[book_index]["title"], new_status)
        return output_message, 0
