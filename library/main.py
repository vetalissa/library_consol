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

    while True:

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