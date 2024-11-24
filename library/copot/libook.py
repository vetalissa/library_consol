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

    def __init__(self, title: str, author: str, year: str, status: str = "В наличии"):
        self.id = self.__id
        self.title = title.capitalize()
        self.author = author.title()
        self.year = year
        self.status = status

    def __setattr__(self, key, value):
        """ Проверка корректности присваемых значений. """

        if not value:
            print('_' * 165 + '\n')
            print("INFO: Пустые значения недопустимы!")
            self.__reset_id()
            raise ValueError("Пустое значение не допускается.")

        if key == 'year':
            if not value.isdigit() or not (1445 <= int(value) <= datetime.now().year):
                print('_' * 165 + '\n')
                print("INFO: Неверный год, он может содержать только цифры и быть с 1445 по наше время!")
                self.__reset_id()
                raise ValueError("Неверный год книги.")

        object.__setattr__(self, key, value)

    @classmethod
    def __reset_id(cls):
        if cls.__id != 0:
            cls.__id -= 1

    def __str__(self):
        return f'#{self.id}: "{self.title}", {self.author}, {self.year} год, {self.status}'

    def display_book(self) -> str:
        """ Функция отображения книги в виде строки. """
        return ' '.join([self.title.lower(), self.author.lower(), self.year])


class Library:
    """
    Класс библиотека, который работает с классом Book.
    Хранит в себе экземпляры книг и работает с ними.
    """

    def __init__(self):
        self.library = {}

    def add_book(self, title: str, author: str, year: str, status: str = "В наличии") -> Book:
        """ Создание и Добавление новых книг. """

        book = Book(title, author, year, status)
        self.library[book.id] = book
        return book

    def delete_book(self, id_book: int) -> Book:
        """ Удаление книги. """
        book = self.library[id_book]
        del self.library[id_book]
        return book

    def display_books(self) -> None:
        """ Отображение всей библиотеки. """

        print(
            f"{'id'.ljust(5)}|{'Название'.ljust(70)}|{'Автор'.ljust(50)}" +
            f"|{'Год издания'.ljust(10)}|{'Статус'.ljust(20)}|")
        print('_' * 165)

        for i in self.library.values():
            print(
                f'{str(i.id).ljust(5)}|{i.title.ljust(70)}|{i.author.ljust(50)}' +
                f'|{i.year.ljust(11)}|{i.status.ljust(20)}|')
            print('_' * 165)

    def search_book(self, search: str) -> int:
        """ Поиск ключевого слова в библиотеки. """

        count_search = 0  # Счетчик найденных книг

        for i in self.library.values():
            if search.lower() in i.display_book():
                print(
                    f'{str(i.id).ljust(5)}|{i.title.ljust(70)}|{i.author.ljust(50)}' +
                    f'|{i.year.ljust(10)}|{i.status.ljust(20)}|')
                print('_' * 165)
                count_search += 1

        return count_search

    def update_book(self, id_book: int, status: str) -> str:
        """ Изменение статуса объекта Book. """

        if self.library[id_book].status == status:
            return f'Статус книги неизменён, так как книга и так уже {status}\n{self.library[id_book]}'

        self.library[id_book].status = status

        return f'Статус книги изменён на "{status}"\n{self.library[id_book]}'

    @staticmethod
    def check_status(status: str) -> str:
        """ Проверка правильного значения для "status". """

        if 'в наличии' == status.lower():
            status = 'В наличии'
        elif 'выдана' == status.lower():
            status = 'Выдана'
        else:
            raise ValueError
        return status

    def check_id_book(self, id_book: str) -> int:
        """ Проверка индекса. """

        try:
            id_book = int(id_book)
            if id_book not in self.library:
                raise KeyError
        except ValueError:
            raise ValueError

        return id_book
