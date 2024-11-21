from datetime import datetime


class Book:
    """
    Класс книга, содержит в себе всю информацию об объекте:
    уникальный идентификатор, название, автор, год выпуска.
    """
    __id = 0

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        return super().__new__(Book)

    def __init__(self, title: str, author: str, year: str):
        self.id = self.__id
        self.title = title.capitalize()
        self.author = author.title()
        self.year = year
        self.status = "В наличии"

    def __setattr__(self, key, value):
        """ Проверка корректности атрибута 'year'. """
        if key == 'year':
            if 1445 > int(value) or int(value) > datetime.now().year:
                print("Неверный год, он может быть с 1445 по наше время.")
                raise TypeError
        object.__setattr__(self, key, value)

    def __str__(self):
        return f'#{self.id}: "{self.title}", {self.author}, {self.year} год, {self.status}'

    def display_book(self):
        """ Функция отображения книги в виде строки. """
        return ' '.join([self.title.lower(), self.author.lower(), self.year])


class Library:
    """
    Класс библиотека, который работает с классом Book.
    Хранит в себе экземпляры книг и работает с ними.
    """

    def __init__(self):
        self.library = {}

    def add_book(self, title: str, author: str, year: str) -> Book:
        """ Создание и Добавление новых книг. """
        book = Book(title, author, year)
        self.library[book.id] = book
        return book

    def delete_book(self, id_book: int) -> Book:
        book = self.library[id_book]
        del self.library[id_book]
        return book

    def display_books(self):
        """ Отображение всей библиотеки. """
        print(
            f"{'id'.ljust(5)}|{'Название'.ljust(70)}|{'Автор'.ljust(50)}|{'Год издания'.ljust(2)}|{'Статус'.ljust(20)}|")
        print('_' * 165)
        for i in self.library.values():
            print(
                f'{str(i.id).ljust(5)}|{i.title.ljust(70)}|{i.author.ljust(50)}|{i.year.ljust(10)}|{i.status.ljust(20)}|')
            print('_' * 165)

    def search_book(self, search: str) -> int:
        """ Поиск ключевого слова в библиотеки. """
        count_search = 0
        for i in self.library.values():
            if search in i.display_book():
                print('поиск:', i)
                count_search += 1
        return count_search

    def update_book(self, id_book: int, status: str) -> str:
        """ Изменение статуса объекта Book"""
        if self.library[id_book].status == status:
            return f'Статус книги неизменён, так как книга и так уже {status}\n{self.library[id_book]}'

        self.library[id_book].status = status

        return f'Статус книги изменён на "{status}"\n{self.library[id_book]}'

    @staticmethod
    def check_status(status: str) -> str:
        """ Проверка правильного значения для "status". """
        if 'в наличии' == status.lower():
            status = '"В наличии"'
        elif 'выдана' == status.lower():
            status = ' Выдана'
        else:
            raise ValueError
        return status

    def check_id_book(self, id_book: str) -> int:
        """ Проверка индекса """
        try:
            id_book = int(id_book)
            if id_book not in self.library:
                raise KeyError
        except ValueError:
            raise ValueError

        return id_book
