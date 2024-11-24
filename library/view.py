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