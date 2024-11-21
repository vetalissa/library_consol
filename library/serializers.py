import json
from libook import Book


def create_json_library():
    """
    Создание пустого файла json.
    Если у вас нет, файла json c книгами, вы можете создать пустой.
    И с помощью консоли и команды "Добавить" заполнить библиотеку.
    """
    with open('data.json', 'w', encoding='utf-8') as file_data:
        json.dump({}, file_data, ensure_ascii=False, indent=4)


def load_json_library(library):
    """
    Загрузка книг из json.
    """


def add_json_library(book_instance: Book):
    """
    Добавление книг в json.
    """


def update_json_library(id_book: int, status: str):
    """
    Обновление статуса у книги в json.
    """


def delete_json_library(id_book: int):
    """
    Удаление книги из json.
    """


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
