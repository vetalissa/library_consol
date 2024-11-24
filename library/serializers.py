import json

from libook import Book, Library


def manage_json_file(name_file: str, data: dict = None) -> dict:
    """
    Управление файлом JSON: чтение или запись.
    Если data не передан, происходит чтение.
    Если data передан, происходит запись.
    """
    if data is not None:  # Запись
        with open(name_file, 'w', encoding='utf-8') as json_data:
            json.dump(data, json_data, ensure_ascii=False, indent=4)
    else:  # Чтение
        with open(name_file, 'r', encoding='utf-8') as json_data:
            return json.load(json_data)


def load_json_library(name_file: str, library: Library):
    """
    Загрузка книг из json, дополнительно происходит перезапись файла для корректной работы.
    """
    try:
        data = manage_json_file(name_file)  # Выгружаем данные из файла
        data2 = {}  # Обновленный словарь

        for book in data.values():
            book_title = book['title']
            book_author = book['author']
            book_year = book['year']
            book_status = book['status']

            # Создаем экземпляр класса Book и добавляем в Library
            book_instance = library.add_book(book_title, book_author, book_year, book_status)
            data2[book_instance.id] = book_instance.__dict__

        # Перезаписываем json файл
        manage_json_file(name_file, data2)

    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден.")


def add_json_library(name_file: str, book_instance: Book):
    """
    Добавление книг в json.
    """
    try:
        data = manage_json_file(name_file)  # Выгружаем данные из файла
        data[book_instance.id] = book_instance.__dict__  # Добавляем новую книгу

        # Записываем в файл
        manage_json_file(name_file, data)

    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка при обработке JSON: {e}")


def update_json_library(name_file: str, id_book: int, status: str):
    """
    Обновление статуса у книги в json.
    """
    try:
        data = manage_json_file(name_file)  # Выгружаем данные из файла
        data[str(id_book)]['status'] = status  # Меняем статус

        # Запись в json
        manage_json_file(name_file, data)

    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка при обработке JSON: {e}")


def delete_json_library(name_file: str, id_book: int):
    """
    Удаление книги из json.
    """
    try:
        data = manage_json_file(name_file)  # Выгружаем данные из файла

        del data[str(id_book)]

        # Записываем в файл
        manage_json_file(name_file, data)

    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка при обработке JSON: {e}")
