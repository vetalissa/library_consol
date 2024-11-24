from copot import view


def start():
    command = '''Список команд:
        Добавить книгу в библиотеку: "Добавить"
        Вывести список всех книг: "Список"
        Удалить книгу из библиотеки: "Удалить"
        Изменить статус книги: "Статус"
        Найти книгу: "Поиск"
        Для выхода в главное меню напишите: "МЕНЮ" обязательно капсом!
        Для выхода из приложения напишите: "ВЫХОД" обязательно капсом!'''

    while True:
        print('_' * 165)
        print(command)
        print('_' * 165)
        command_text = input("Введите команду: ")
        while True:

            if command_text.lower() == 'добавить':
                view.library_add_book()
                break
            elif command_text.lower() == 'удалить':
                view.library_remove_book()
                break
            elif command_text.lower() == 'список':
                view.library.display_books()
                break

            elif command_text.lower() == 'статус':
                view.library_update_book()
                break
            elif command_text.lower() == 'поиск':
                view.library_search_book()
                break
            elif command_text in ('МЕНЮ', 'ВЫХОД'):
                print('\n' * 50)
                break

            else:
                print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
                print("Такой команды не существует.")
                print('<!>' * 55 + '\n')
                break

        if command_text == 'ВЫХОД':
            # Команда для выхода и закрытия приложения

            answer = input('Вы уверены что хотите выйти из Библиотеки?(ДА/НЕТ)')
            if answer == 'ДА':
                print('До свидания!')
                break


if __name__ == '__main__':
    view.create_or_load_json()
    start()
