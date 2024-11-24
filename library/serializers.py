import json
import os

from libook import Book, Library


def manage_json_file(name_file: str, data: dict = None) -> dict:
    """
    Управление файлом JSON: чтение или запись.
    Если data не передан, происходит чтение.
    Если data передан, происходит запись.
    """
    # Папка с файлами JSON
    directory = "data_library"

    # Полный путь к файлу
    file_path = os.path.join(directory, name_file)

    if data is not None:  # Запись
        with open(file_path, 'w', encoding='utf-8') as json_data:
            json.dump(data, json_data, ensure_ascii=False, indent=4)
    else:  # Чтение
        with open(file_path, 'r', encoding='utf-8') as json_data:
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


def check_file_name(name_file: str):
    """
    Проверка формата названия файла JSON.
    """
    if not name_file.endswith('.json'):
        print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
        print("Файл должен иметь расширение .json.")
        print('<!>' * 55 + '\n')
        return False
    return True


def check_file_in_dir(name_file: str, action: str) -> bool:
    """
    Проверка существования файла JSON c переданным названием.
    """
    file_path = "data_library/" + name_file

    if action == 'load':
        if os.path.isfile(file_path):
            return True
        else:
            print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
            print('Файла нет в директории "data_library", проверьте что бы файл находился в папке "data_library"!\n')
            print('<!>' * 55 + '\n')
            return False

    if action == 'create':
        if not os.path.isfile(file_path):
            return True
        else:
            print('\n' + '<>' * 6 + 'ПРЕДУПРЕЖДЕНИЕ' + '<>' * 69)
            print('Файл с таким именем уже есть в директории "data_library", все данные файла будут удалены!')
            print('<>' * 83 + '\n')
            return False