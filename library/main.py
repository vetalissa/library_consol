import serializers
from libook import Library

library = Library()
name_file = 'data.json'
command = '''Список команд:
    Добавить книгу в библиотеку: "Добавить"
    Вывести список всех книг: "Список"
    Удалить книгу из библиотеки: "Удалить"
    Изменить статус книги: "Статус"
    Найти книгу: "Поиск
    Для выхода в главное меню напишите: "МЕНЮ" обязательно капсом!'''


def hello():
    """
    Функция старта, позволяющая работать с уже имеющемся файлом json или создать новый.
    :return:
    """
    global name_file

    print('Приветствуем Вас в библиотеке!\n'
          'Вы бы хотели продолжить работу с имеющейся библиотекой или создать пустую?\n')
    flag_start = False

    while flag_start != True:
        answer = input('Напишите:\n '
                       '"НОВАЯ", если хотите создать пустую библиотеку\n '
                       '"БИБ", если хотите использовать заполненную библиотеку с книгами\n\n'
                       'Ваш ответ: ')

        if answer == 'НОВАЯ':
            name_file = 'data2.json'

            # Создаем новый пустой файл json
            serializers.create_json_library(name_file)

            flag_start = True
        elif answer == 'БИБ':
            print('Файл json должен называться "data.json" и находиться в корне проекта')
            print('Загружаем библиотеку...\nОжидайте...')

            # Выгружаем из файла data.json все книги
            serializers.load_json_library(name_file, library)

            flag_start = True
        else:
            print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
            print("Такой команды не существует.")
            print('<!>' * 55 + '\n')


def library_add_book():
    """
    Функция добавления книги(Book) в библиотеку(Library).
    """
    global command_text, yes_or_no

    print('_' * 165)

    book_val = {
        'book_title': ['Введите название книги: ', ''],
        'book_author': ['Введите автора: ', ''],
        'book_year': ['Введите год издания: ', '']
    }

    try:
        for key in book_val:
            val = input(book_val[key][0])

            if val == 'МЕНЮ':  # Выход в меню
                command_text = 'МЕНЮ'
                return False

            book_val[key][1] = val
        else:
            book = library.add_book(book_val['book_title'][1], book_val['book_author'][1],
                                    book_val['book_year'][1])

            serializers.add_json_library(name_file, book)  # Добавление в файл data.json новой книги

            print('_' * 165)
            print(f'{book}\nКнига успешна добавлена в библиотеку.')

            yes_or_no = input('Добавить еще одну книгу?(Да/Нет)\n')

    except TypeError:
        print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
        print('Вы ввели неверные данные...\nПопробуйте ещё раз.')
        print('<!>' * 55 + '\n')


def library_remove_book():
    """
    Функция удаление книги(Book) из библиотеки(Library).
    """
    global command_text, yes_or_no

    # print('_' * 165)
    input_id_book = input('Напишите индекс(номер) книги, которую вы хотите удалить:\n')

    if input_id_book == 'МЕНЮ':  # Выход в меню
        command_text = 'МЕНЮ'
        return False

    try:
        id_book = library.check_id_book(input_id_book)  # Проверка корректности id

        print('\n' + '<>' * 40 + 'ПРЕДУПРЕЖДЕНИЕ' + '<>' * 40)
        you_sure = input('Вы уверены, что хотите удалить книгу?(Да/Нет)\n'
                         f'{library.library[id_book]}\n')
        print('<>' * 85 + '\n')

        if 'да' != you_sure.lower():
            print('Удаление отменено')
            print('_' * 165)
            yes_or_no = input('Хотите удалить другую книгу?(Да/Нет)\n')
            return False

        book = library.delete_book(id_book=id_book)

        serializers.delete_json_library(name_file, id_book)  # Удаление из файла data.json книги

        print('_' * 165)
        print(f'Книга: {book}\nБыла успешна удалена!')

        yes_or_no = input('Удалить еще одну книгу?(Да/Нет)\n')

    except KeyError:
        print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
        print(
            'Индекс {input_id_book} отсутствует у нас в библиотеке.\n'
            'Попробуйте ввести другой индекс и/или проверьте его в библиотеке.'
        )
        print('<!>' * 55 + '\n')
    except ValueError:
        print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
        print(
            'Такого индекса не существует, проверьте чтобы введенный индекс был числом\n'
            'и присутствовал у нас в библиотеке.'
        )
        print('<!>' * 55 + '\n')


def library_update_book():
    """
        Функция изменения статуса книги(Book).
    """
    global command_text, yes_or_no

    # Флаги позволяющие вводить поочередно id, а после status.
    f1 = False
    f2 = False

    while f1 != True:
        # Будем вводить id пока не введем достоверный id или не решим выйти("Меню").
        print('_' * 165)
        input_id_book = input('Напишите индекс(номер) книги у которой хотите изменить статус:\n')
        try:

            if input_id_book == 'МЕНЮ':  # Выход в меню
                command_text = 'МЕНЮ'
                return False

            id_book = library.check_id_book(input_id_book)  # Проверка корректности id
            f1 = True  # Меняем флаг, для перехода к следующему input нового статуса

        except KeyError:
            print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
            print(
                f'Индекс {input_id_book} отсутствует у нас в библиотеке.\n'
                'Попробуйте ввести другой индекс и/или проверьте его в библиотеке.')
            print('<!>' * 55 + '\n')
        except ValueError:
            print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
            print(f'Неверно указан индекс! "{input_id_book}" не является числом!')
            print('<!>' * 55 + '\n')

    while f2 != True and f1 == True:
        # Будем вводить status пока не введем достоверный status или не решим выйти("Меню").

        print('\n' + '<>' * 40 + 'ПРЕДУПРЕЖДЕНИЕ' + '<>' * 40)
        print('Вы хотите изменить статус книги:\n'
              f'{library.library[id_book]}')
        print('<>' * 85 + '\n')

        try:
            input_status = input('Напишите новый статус, он может быть только "В наличии" или "Выдана"\n'
                                 '~ Если вы перепутали id -> "Назад"\n')

            if input_status == 'МЕНЮ':  # Выход в меню
                command_text = 'МЕНЮ'
                return False

            if input_status.lower() == 'назад':
                f1 = False
                return False

            status = library.check_status(input_status)  # Проверка корректности status
            answer_update = library.update_book(id_book, status)  # Обновление статуса

            serializers.update_json_library(id_book, status)  # Изменение статуса книги в файле data.json

            print('_' * 165)
            print(answer_update)  # Вывод обновленной книги
            print('_' * 165)

            f2 = True
            yes_or_no = input('Изменить ещё статус?(Да/Нет)\n')

        except ValueError:
            print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
            print(f'Статус указан неверно! Укажите правильно: "В наличии" или "Выдана"')
            print('<!>' * 55 + '\n')


def library_search_book():
    """
        Функция поиска книги(Book) по ключевому слову.
    """
    global command_text, yes_or_no
    print('\n' + '_' * 82 + 'ПОИСК' + '_' * 82)
    input_search = input('Введите название, автора или год издания для поиска:\n')

    if input_search == 'МЕНЮ':  # Выход в меню
        command_text = 'МЕНЮ'
        return False

    print('_' * 165)
    response = library.search_book(input_search)  # Вывод найденных совпадений -> количество ответов.
    print(f'Найдено:{response}')  # Вывод количество ответов
    print('_' * 165)

    yes_or_no = input('Искать ещё?(Да/Нет)\n')


hello() # Создание или закачка библиотеки из файла json
# Бесконечная работа консоли
while True:
    print('_' * 165)
    print(command)
    print('_' * 165)

    command_text = input("Введите команду: ")
    yes_or_no = 'да'  # Флаг работы команды.

    while True and yes_or_no.lower() != 'нет':

        if command_text.lower() == 'добавить':
            library_add_book()

        elif command_text.lower() == 'удалить':
            library_remove_book()

        elif command_text.lower() == 'список':
            library.display_books()
            break

        elif command_text.lower() == 'статус':
            library_update_book()

        elif command_text.lower() == 'поиск':
            library_search_book()

        elif command_text == 'МЕНЮ':
            print('\n' * 50)
            break

        else:
            print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
            print("Такой команды не существует.")
            print('<!>' * 55 + '\n')
            break
