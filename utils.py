def load_books():
    """Загружаем книги из файла"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_books(books):
    """Сохраняем книги в файл"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f)


def search_books(books):
    """Ищем книги по названию"""
    print("\n--- Поиск книги ---")

    search_term = input("Введите часть названия для поиска: ").strip().lower()
    if not search_term:
        print("Ошибка: Введите текст для поиска")
        return

    found_books = []
    for book in books:
        if search_term in book["title"].lower():
            found_books.append(book)

    if not found_books:
        print("Книги не найдены")
        return

    print(f"Найдено {len(found_books)} книг:")
    for i, book in enumerate(found_books, 1):
        status = "Прочитана" if book["read"] else "Не прочитана"
        print(f"{i}. '{book['title']}' - {book['author']} ({status})")


def update_read_status(books):
    """Обновляем статус книги"""
    print("\n--- Обновление статуса книги ---")

    if not books:
        print("В библиотеке нет книг")
        return

    show_all_books(books)

    try:
        book_num = int(input("\nВведите номер книги для обновления статуса: "))
        if book_num < 1 or book_num > len(books):
            print("Ошибка: Неверный номер книги")
            return

        book = books[book_num - 1]
        book["read"] = not book["read"]

        save_books(books)
        status = "прочитана" if book["read"] else "не прочитана"
        print(f"Статус книги '{book['title']}' изменен на '{status}'")


    except ValueError:
        print("Ошибка: Введите корректный номер")


def show_all_books(books):
    """Выводим все книги"""
    if len(books) > 0:
        for number, book in enumerate(books, 1):
            print(f'\nКнига - {number}\nНазвание: {book['title']}\n'
                  f'Автор: {book['author']}\n'
                  f'Статус: {'прочитана' if book['read'] else 'не прочитана'}\n')
            print('----------------------------------')
    else:
        print('\nСписок книг пуст.')


def add_book(books):
    """Добавляем книгу"""
    title = input('\nВведите название книги: ')
    author = input('Введите автора книги: ')

    new_book = {
        "title": title,
        "author": author,
        "read": False}

    books.append(new_book)
    save_books(books)
    print(f'\nКнига "{title}" добавлена.')


def delete_book(books):
    """Удаляем книгу"""
    while True:

        show_all_books(books)

        try:
            index = int(input('\nВведите номер книги для удаления: '))
            if 1 <= index <= len(books):
                del_book = books[index - 1]['title']
                books.pop(index - 1)
                save_books(books)
                print(f'\nКнига "{del_book}" удалена.')
                break
            else:
                print('\nКниги под таким номером не существует.\n')
        except ValueError:
            print('\nДанный ввод не является целым числом.\n')
