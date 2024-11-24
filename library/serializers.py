import json

from libook import Book, Library


def create_json_library(name_file: str):
    """
    Создание пустого файла json.
    Если у вас нет, файла json c книгами, вы можете создать пустой.
    И с помощью консоли и команды "Добавить" заполнить библиотеку.
    """

    with open(name_file, 'w', encoding='utf-8') as json_data:
        json.dump({}, json_data, ensure_ascii=False, indent=4)


def load_json_library(name_file: str, library: Library):
    """
    Загрузка книг из json, дополнительно происходит перезапись файла для корректной работы.
    """
    try:
        data = unloading_json(name_file)  # Выгружаем данные из файла
        data2 = {}
        for book in data.values():
            book_title = book['title']
            book_author = book['author']
            book_year = book['year']
            book_status = book['status']

            # Создаем экземпляр класса Book и добавляем в Library
            book_instance = library.add_book(book_title, book_author, book_year, book_status)
            data2[book_instance.id] = book_instance.__dict__

        # Перезаписываем json файл
        create_json_library(name_file)
        loading_in_json(name_file, data2)
    except FileNotFoundError:
        raise FileNotFoundError


def add_json_library(name_file: str, book_instance: Book):
    """
    Добавление книг в json.
    """
    try:
        data = unloading_json(name_file)  # Выгружаем данные из файла
        data[book_instance.id] = book_instance.__dict__

        # Записываем в файл
        loading_in_json(name_file, data)

    except json.JSONDecodeError as e:
        print(f"Ошибка при обработке JSON: {e}")


def update_json_library(name_file: str, id_book: int, status: str):
    """
    Обновление статуса у книги в json.
    """
    try:
        data = unloading_json(name_file)  # Выгружаем данные из файла
        data[str(id_book)]['status'] = status  # Меняем статус

        # Запись в json
        loading_in_json(name_file, data)

    except json.JSONDecodeError as e:
        print(f"Ошибка при обработке JSON: {e}")


def delete_json_library(name_file: str, id_book: int):
    """
    Удаление книги из json.
    """
    try:
        data = unloading_json(name_file)  # Выгружаем данные из файла

        # Удаление книги
        del data[str(id_book)]

        # Запись в json
        loading_in_json(name_file, data)

    except json.JSONDecodeError as e:
        print(f"Ошибка при обработке JSON: {e}")


def unloading_json(name_file: str) -> dict:
    """
    Выгружаем данные из файла json.
    """
    with open(name_file) as json_data:
        data = json.load(json_data)

    return data


def loading_in_json(name_file: str, data: dict):
    """
    Загружаем данные в файла json.
    """

    with open(name_file, 'w') as json_data:
        json.dump(data, json_data, ensure_ascii=False, indent=4)
