# О проекте:

Пэт-проект.
Консольное приложение написанное на `Python`. Представляет из себя библиотеку с книгами.

## Функционал:
- Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
- Удаление книги: Пользователь вводит id книги, которую нужно удалить.
- Поиск книги: Пользователь может искать книги по title, author или year.
- Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
- Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).
- Сохранение в json файл всех книг.
- Загрузка книг из json файла.
- Обновление книг в json файла.
- Удаление книг из json файла.



# JSON:

Для того что бы запустить проект, вы можете использовать готовый файл `data.json`.
Он содержит в себе 100 книг.

Если у вас есть свой файл json c книгами, вы можете поместить его в проект с названием `data.json`.
Если вы хотите начать работу с пустой библиотекой, при запуске у вас будет возможность создать пустой json.

#### Вот такая должна быть структура json файла:

```json
{
    "1": {
        "id": 1,
        "title": "Посторонний",
        "author": "Альбер Камю",
        "year": "1942",
        "status": "В наличии"
    },
    "2": {
        "id": 2,
        "title": "В поисках утраченного времен",
        "author": "Марсель Пруст",
        "year": "1913",
        "status": "В наличии"
    },
    "3": {
        "id": 3,
        "title": "Процесс",
        "author": "Франц Кафка",
        "year": "1925",
        "status": "В наличии"
    }
}
```

#### Запуск приложения:

Вы можете воспользоваться IDE и запустить файл `main.py`.

Для запуска приложения из консоли: нужно перейти в каталог с файлами приложения и запустить командой:

```python
python3 main.py
```

### Старт

При запуске, вам нужно указать: хотите ли вы использовать пустую библиотеку или закачать данные из фала json.

### Команды и как они работаю:

Для того чтобы удобно пользоваться приложением, существуют ключевые слова. Вам достаточно их написать и следовать дальнейшим указаниям.


### Ошибки

Если где-то Вы совершили ошибку, вам высветиться специальное окошко, в котором будет прописано, что случилось.


### Предупреждение

Если вы совершаете удаление или изменение статуса, вам предупредят, об уточнение указанных действий.


### Вид Библиотеки

Вот так выглядит вывод всех книг при команде `Список`:


### Вид результата поиска

Поиск ищет указанный текст в title, author, year.
Вот так выглядит вывод найденных совпадений при команде `Поиск`:


### Выход

Для того чтобы выйти обратно в меню, достаточно написать `МЕНЮ` в большинстве окошек ввода.
Если это окно ввода с вопросом `Да/Нет`, то вам нужно написать `Нет` для выхода в меню.

Если вы хотите закрыть приложение полностью напиши `ВЫХОД`, так приложение закончит свою работу.

