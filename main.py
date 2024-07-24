from library.library import BookRepository


def library_operation():
    """Handles input operations"""

    library = BookRepository()
    operation = "start"
    while operation != "exit":
        operation = input("Введите команду: ")
        if operation == "get":
            print(library.get())

        elif operation == "get author":
            author = input("Введите имя автора: ")
            while not author:
                print("Недопустимо пустое имя автора")
                author = input("Введите имя автора: ")
            books, _ = library.get_by("author", author)
            print(books)

        elif operation == "get year":
            err = True
            while err:
                books, err = library.get_by("year", input("Введите год издания (после 1457): "))
                print(books)

        elif operation == "get title":
            title = input("Введите нзвание книги: ")
            while not title:
                print("Недопустимо пустое название книги")
                title = input("Введите нзвание книги: ")

            books, _ = library.get_by("title", title)
            print(books)

        elif operation == "add":
            title = input("Введите нзвание книги: ")

            while not title:
                print("Недопустимо пустое название книги")
                title = input("Введите нзвание книги: ")
            author = input("Введите имя автора: ")
            while not author:
                print("Недопустимо пустое имя автора")
                author = input("Введите имя автора: ")
            err = 1
            while err:
                year = input("Введите год издания (после 1457): ")
                books, err = library.add(title, author, year)
                print(books)

        elif operation == "update":
            book_id = input("Введите id книги: ")
            new_status = input("Введите новый статус книги ('выдана'/'в наличии'): ")
            books, err = library.update(book_id, new_status)
            print(books)
            while err:
                if err == 2:
                    book_id = input("Введите id книги: ")
                else:
                    new_status = input("Введите новый статус книги ('выдана'/'в наличии'): ")
                books, err = library.update(book_id, new_status)
                print(books)

        elif operation == "delete":
            err = True
            while err:
                book_id = input("Введите id книги: ")
                books, err = library.delete(book_id)
                print(books)

        elif operation != "exit":
            print("Недопустимая команда")


if __name__ == "__main__":
    library_operation()
