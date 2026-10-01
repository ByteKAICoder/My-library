import utils

def main():
    """Основная функция программы"""
    print("Добро пожаловать в библиотеку!")

    # Загружаем книги из файла
    books = utils.load_books()

    while True:
        utils.show_menu()

        choice = input("\nВыберите действие (1-6): ").strip()

        if choice == "1":
            utils.show_all_books(books)
        elif choice == "2":
            utils.add_book(books)
        elif choice == "3":
            utils.search_books(books)
        elif choice == "4":
            utils.update_read_status(books)
        elif choice == "5":
            utils.delete_book(books)
        elif choice == "6":
            print("\nДо свидания! Ваши книги сохранены.")
            break
        else:
            print("Ошибка: Неверный выбор. Введите число от 1 до 6")

main()
