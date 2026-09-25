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
