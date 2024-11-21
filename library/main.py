from libook import Library
import serializers

library = Library()

print('Загружаем библиотеку...\nОжидайте...')

# Выгружаем из файла data.json все книги
serializers.load_json_library(library)

command = '''Список команд:                                                                                                                                        
    Добавить книгу в библиотеку: "Добавить"                                                                                                                            
    Вывести список всех книг: "Список"                                                                                                                             
    Удалить книгу из библиотеки: "Удалить"                                                                                                                             
    Изменить статус книги: "Статус"                                                                                                                                    
    Найти книгу: "Поиск
    Для выхода в главное меню напишите: "МЕНЮ" '''

print('Приветствуем Вас в библиотеке!\n')

def library_add_book():
    """
    Функция добавления книги(Book) в библиотеку(Library).
    """
    global command_text, yes_or_no

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

            serializers.add_json_library(book) # Добавление в файл data.json новой книги

            print('_' * 165)
            print(f'{book}\nКнига успешна добавлена в библиотеку.')

            yes_or_no = input('Добавить еще одну книгу?(Да/Нет)\n')

    except TypeError:
        print('Вы ввели неверные данные...\nПопробуйте ещё раз.')
        print('_' * 165)


def library_remove_book():
    """
        Функция удаление книги(Book) из библиотеки(Library).
    """
    global command_text, yes_or_no

    print('_' * 165)
    input_id_book = input('Напишите индекс(номер) книги, которую вы хотите удалить:\n')

    if input_id_book == 'МЕНЮ':  # Выход в меню
        command_text = 'МЕНЮ'
        return False

    try:
        id_book = library.check_id_book(input_id_book)  # Проверка корректности id

        you_sure = input(f'Вы уверены, что хотите удалить книгу?(Да/Нет)\n {library.library[id_book]}\n')
        if 'да' != you_sure.lower():
            print('Удаление отменено')
            return False

        book = library.delete_book(id_book=id_book)

        serializers.delete_json_library(id_book) # Удаление из файла data.json книги


        print('_' * 165)
        print(f'Книга: {book}\nБыла успешна удалена!')

        yes_or_no = input('Удалить еще одну книгу?(Да/Нет)\n')

    except KeyError:
        print(
            f'Индекс {input_id_book} отсутствует у нас в библиотеке.\nПопробуйте ввести другой индекс и/или проверьте его в библиотеке.')
    except ValueError:
        print(
            'Такого индекса не существует, проверьте чтобы введенный индекс был числом\nи присутствовал у нас в библиотеке.')


def library_update_book():
    """
        Функция изменения статуса книги(Book).
    """
    global command_text, yes_or_no

    # Флаги позволяющие вводить поочередно id, а после status.
    f1 = False
    f2 = False

    while f1 != True:
        # Будем вводить id пока не решим выйти("Меню") или не введем достоверный id.
        input_id_book = input('Напишите индекс(номер) книги у которой хотите изменить статус\n')
        try:

            if input_id_book == 'МЕНЮ':  # Выход в меню
                command_text = 'МЕНЮ'
                return False

            id_book = library.check_id_book(input_id_book)  # Проверка корректности id
            f1 = True  # Меняем флаг, для перехода к следующему input нового статуса

        except KeyError:
            print(
                f'Индекс {input_id_book} отсутствует у нас в библиотеке.\nПопробуйте ввести другой индекс и/или проверьте его в библиотеке.')
        except ValueError:
            print(f'Неверно указан индекс! "{input_id_book}" не является числом!')

    while f2 != True and f1 == True:
        # Будем вводить status пока не введем достоверный id или не решим выйти("Меню").
        try:
            input_status = input('Напишите новый статус, он может быть только "В наличии" или "Выдана"\n')

            if input_status == 'МЕНЮ':  # Выход в меню
                command_text = 'МЕНЮ'
                return False

            status = library.check_status(input_status)  # Проверка корректности status
            answer_update = library.update_book(id_book, status)  # Обновление статуса

            serializers.update_json_library(id_book, status) # Изменение статуса книги в файле data.json


            print(answer_update)  # Вывод обновленной книги
            print('_' * 165)

            f2 = True
            yes_or_no = input('Изменить ещё статус?(Да/Нет)\n')

        except ValueError:
            print(f'Статус указан неверно! Укажите правильно: "В наличии" или "Выдана"')


def library_search_book():
    """
        Функция поиска книги(Book) по ключевому слову.
    """
    global command_text, yes_or_no

    input_search = input('Введите название, автора или год издания для поиска:\n')

    if input_search == 'МЕНЮ':  # Выход в меню
        command_text = 'МЕНЮ'
        return False

    print('_' * 165)
    response = library.search_book(input_search)  # Вывод найденных совпадений -> количество ответов.
    print(f'Найдено:{response}')  # Вывод количество ответов
    print('_' * 165)

    yes_or_no = input('Искать ещё?(Да/Нет)\n')



# Бесконечная работа консоли
while True:
    print('_' * 165)
    print(command)
    print('_' * 165)

    command_text = input("Введите команду: ")
    yes_or_no = 'да' # Флаг работы команды.

    while True and yes_or_no.lower() == 'да':

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
            break

        else:
            print("Такой команды не существует.")
            break