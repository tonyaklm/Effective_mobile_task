### Тестовое задание для Effective Mobile
Для запуска программы из корня директории написать `python main.py`

После запуска программы, приложение начинает обрабатывать приходящие запросы, пока не будет введена операция `exit`.

## 1. Доступные названия операций:

* `get` - Отображение всех книг

* `get author` - Поиск книги по автору

  Аргументы:

    - Имя автора для поиска : str

* `get title` - Поиск книги по автору

  Аргументы:

    - Название книги для поиска : str

* `get year` - Поиск книги по году

  Аргументы:

    - Год издания книги для поиска : int

* `add` - Добавление книги

  Аргументы:

    - `title`: str - Название книги
    - `author`: str - Автор книги
    - `year`: int - Год издания (от 1457 до 2024)

* `delete` - Удаление книги

  Аргументы:

    - `book_id`: int - id книги по котрой происходит удаление

* `update` - Изменение статуса книги

  Аргументы:

    - `book_id`: int - id книги для которой изменяется статус
    - `new_status`: str - Новый статус книги

* `exit` - Завершение потока команд:

После ввода названия операции командная строка подсказывает какой ожидается ввод, а именно в каком порядке аргументы
должены поступить.

## 2. Структура проекта:

### 2.1 main.py

В файле лежит код для запуска самого приложения и обработки поступивших команд

### 2.2 library/book.py

В файле лежит код для класса книги, она создается по title, year, author и id, который вычисляется как максимальный id
из существующих книг + 1,

### 2.3 library/library.py (Основные функции)

В файле лежит код для класса библиотеки,в котором и находятся все необходимые операции
добавления/удаления/обновления/поиска
<details>
  <summary>Методы класса BookRepository</summary>

#### 2.3.1 `get() -> str`

Ничего не принимает на вход и возвращает все книги в стрковом представлении для вывода. Открывает файл с книгами на
чтение и преобразует их.

#### 2.3.2 `get_by(search_key: str, search_value: str) -> (str, bool)`

Принимает на вход ключ для поиска (author, year, title) и значения для фильтрации, возвращает строку с подходящими по
критериям посика списком книг. По author и year совпадением читается наличие введенного названия в названии книги, а по
year ищет полное совпадение. Открывает файл с книгами, проходится по ним и берет подходящие. Возвращает строчку с
описанием книг и True - если во время выполнения возникла ошибка, False - если не возникала.

#### 2.3.3 `add(title: str, author: str, year: str) -> (str, bool)`

Принимает на вход название книги, автора и год. Читает данные из файла библиотеки, берет максимальный id + 1 для новой
книги, а если это первая книга, то id = 1. Добавляет новую книгу в список JSON'ов и запысывает изменения. Год
проверяется на тип int и на дату в промежутке 1457 - 2024. В конце отправляет сообщение с подтверждением об успешном
добавлении/ошибке, а также True/False - была ли ошибка во время программы, для того чтобы повторить ввод данных для
пользователя.

#### 2.3.4 `delete(book_id: str) -> (str, bool)`

Принимает на вход id книги, которую надо удалить. Читает данные из библиотеки, удаляет необходимый элемент и записывает
обратно в файл изменения. Есть проверка на корректный тип данных book_id (int) и на наличие книги в библиотеке.
Возвращает ответ об успешном удалении/ошибке, а также True/False - была ли ошибка во время программы, для того чтобы
повторить ввод данных для пользователя.

#### 2.3.4 `update(book_id: str, new_status: str) -> (str, int)`

Принимает на вход id книги, для которой надо поменять статус и новый статус. Читает данные, меняет статус у книги и
записывает данные обратно. Есть проверка на корректный тип данных book_id (int) и на наличие книги в библиотеке.
Возвращает сообщение об успешном обновлении статуса/ошибке, а также 0 - не было ошибок во время выполнения, 1 - ошибка
из-за статуса, который может быть только "в наличии/выдана", 2 - ошибка возникла из-за поступившего id.
</details>

### 2.4 library/utils.py (Вспомогательные функции)

В данном файле лежат вспомогательные функции для открытия/закрытия файла с книгами, конвертация списка JSON'ов в строку
и функция поиска книги в библиотеки по ее id.

<details>
  <summary>Впомогательные функции</summary>

#### 2.4.1 `open_file() -> List[Dict]`

Открывает файл с книгами, если его еще не существует, то создает его и возвращает список JSON'ов.

#### 2.3.2 `write_to_file(books: List[Dict]) -> None`

Записывает поступивший список JSON'ов в файл.

#### 2.3.3 `find_book(books: List[Dict], book_id: int) -> int`

Ищет индект книги в списке по ее id, если такой нет в списке, возвращает -1.

#### 2.3.4 `print_books(books: List[Dict]) -> str`

Преобразует список JSON'ов в строку для красивого представления пользователю.

</details>

### 2.5 library/constants.py

В файле лежит всего одна константа - относительный путь к файлу, в который будут сохранятся книги. "data/library.json"
