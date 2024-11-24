import serializers
from libook import Library

library = Library()
name_file = 'data.json'


def get_file_name(action):
    """ Запрос у пользователя названия файла, и проверка его формата и наличия в директории. """
    while True:
        name_file = input("Введите название файла (с расширением .json): ")

        if serializers.check_file_name(name_file):  # Проверка формата .json
            if serializers.check_file_in_dir(name_file, action):  # Проверка существования файла
                return name_file
            elif action == 'create':  # Если файл создается, но уже есть в директории
                you_sure = input('Вы уверенны, что хотите удалить все данные из файла?(ДА/НЕТ)\n')
                if you_sure == 'ДА':
                    return name_file


def create_or_load_json():
    """
    Функция старта, позволяющая работать с уже имеющимся файлом JSON или создать новый.
    """
    global name_file

    print('Приветствуем Вас в библиотеке!\n'
          'Вы хотите продолжить работу с имеющейся библиотекой или создать новую?\n')

    while True:
        answer = input('Напишите:\n'
                       '"CREATE", если хотите создать пустую библиотеку\n'
                       '"LOAD", если хотите использовать заполненную библиотеку с книгами\n'
                       '"START", если хотите просто начать использовать приложение :)\n\n'
                       'Ваш ответ: ')

        if answer == 'CREATE':
            # Запрос у пользователя нового имени файла
            name_file = get_file_name('create')

            # Создание нового JSON файла
            serializers.manage_json_file(name_file, {})

        elif answer in ('LOAD', 'START'):
            if answer == 'LOAD':
                # Запрос у пользователя имени файла
                name_file = get_file_name('load')
            else:
                name_file = 'data.json'

            # Выгружаем из файла JSON все книги
            try:
                serializers.load_json_library(name_file, library)
            except ValueError:
                print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
                print('Произошла ошибка при чтении и записи файла, проверьте файл и попробуйте снова')
                print('<!>' * 55 + '\n')
                continue
        else:
            print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
            print("Такой команды не существует.")
            print('<!>' * 55 + '\n')
            continue

        break


def library_add_book():
    """
    Функция добавления книги(Book) в библиотеку(Library).
    """
    while True:
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
                    return

                book_val[key][1] = val
            else:
                book = library.add_book(book_val['book_title'][1],
                                        book_val['book_author'][1],
                                        book_val['book_year'][1])

                serializers.add_json_library(name_file, book)  # Добавление в файл data.json новой книги

                print('_' * 165)
                print(f'{book}\nКнига успешна добавлена в библиотеку.')
                print('_' * 165)

            if 'да' != input('Добавить еще одну книгу?(Да/Нет)\n').lower():
                break

        except ValueError:
            print('\n' + '<!>' * 3 + 'ОШИБКА' + '<!>' * 50)
            print('Вы ввели неверные данные...\nПопробуйте ещё раз.')
            print('<!>' * 55 + '\n')

def library_remove_book():
    """
    Функция удаление книги(Book) из библиотеки(Library).
    """
    while True:
        # Будем вводить id пока не введем достоверный id или не решим выйти("Меню")
        id_book = get_id_book()

        if not id_book:  # Выход в меню
            return

        # Согласие на удаление
        print('\n' + '<>' * 6 + 'ПРЕДУПРЕЖДЕНИЕ' + '<>' * 69)
        you_sure = input('Вы уверены, что хотите удалить книгу?(Да/Нет)\n'
                         f'{library.library[id_book]}\n').lower()
        print('<>' * 83 + '\n')

        if 'да' != you_sure:
            print('Удаление отменено')
            print('_' * 165)
            yes_or_no = input('Хотите удалить другую книгу?(Да/Нет)\n')
            if 'нет' == yes_or_no.lower():
                break
        else:
            book = library.delete_book(id_book=id_book)

            try:
                serializers.delete_json_library(name_file, id_book)  # Удаление книги из файла JSON
                print('_' * 165)
                print(f'Книга "{book}" была успешно удалена!')
                print('_' * 165)
                yes_or_no = input('Хотите удалить еще одну книгу?(Да/Нет)\n').lower()
                if 'да' != yes_or_no:
                    return

            except Exception as e:
                print(f'\n{"<!" * 3} ОШИБКА {"<!" * 50}')
                print(f'Ошибка при удалении книги: {str(e)}.')
                print('<!>' * 55 + '\n')


