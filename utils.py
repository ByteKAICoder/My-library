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
