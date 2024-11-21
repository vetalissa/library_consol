from libook import Library

library = Library()

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


def library_update_book():
    """
        Функция изменения статуса книги(Book).
    """
    global command_text, yes_or_no


def library_search_book():
    """
        Функция поиска книги(Book) по ключевому слову.
    """
    global command_text, yes_or_no



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