import json
from libook import Book, Library


def create_json_library():
    """
    Создание пустого файла json.
    Если у вас нет, файла json c книгами, вы можете создать пустой.
    И с помощью консоли и команды "Добавить" заполнить библиотеку.
    """
    with open('data.json', 'w', encoding='utf-8') as file_data:
        json.dump({}, file_data, ensure_ascii=False, indent=4)


def load_json_library(library: Library):
    """
    Загрузка книг из json.
    """
    data = unloading_json()  # Выгружаем данные из файла

    for book in data.values():
        book_title = book['title']
        book_author = book['author']
        book_year = book['year']

        # Создаем экземпляр класса Book и добавляем в Library
        library.add_book(book_title, book_author, book_year)


def add_json_library(book_instance: Book):
    """
    Добавление книг в json.
    """
    try:
        data = unloading_json()  # Выгружаем данные из файла
        data[book_instance.id] = book_instance.__dict__

        # Записываем в файл
        loading_in_json(data)

    except json.JSONDecodeError as e:
        print(f"Ошибка при обработке JSON: {e}")


def update_json_library(id_book: int, status: str):
    """
    Обновление статуса у книги в json.
    """


def delete_json_library(id_book: int):
    """
    Удаление книги из json.
    """
    try:
        data = unloading_json()  # Выгружаем данные из файла

        # Удаление книги
        del data[str(id_book)]

        # Запись в json
        loading_in_json(data)

    except json.JSONDecodeError as e:
        print(f"Ошибка при обработке JSON: {e}")


def unloading_json() -> dict:
    """
    Выгружаем данные из файла json.
    """
    with open('data.json') as json_data:
        data = json.load(json_data)

    return data


def loading_in_json(data):
    """
    Загружаем данные в файла json.
    """
    with open('data.json', 'w') as json_data:
        json.dump(data, json_data, ensure_ascii=False, indent=4)
