from library import Library

def display_menu():
    print("1. Добавить книгу \n"
          "2. Удалить книгу\n"
          "3. Искать книгу\n"
        "4. Отобразить все книги\n"
        "5. Изменить статус книги\n"
        "0. Выход\n")

def main():
    library = Library()
    while True:
        display_menu()
        choice = input("Введите ваш выбор: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)

        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)

        elif choice == '3':
            query = input("Введите название, автора или год для поиска: ")
            library.search_book(query)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            book_id = int(input("Введите ID книги: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_status(book_id, new_status)

        elif choice == '0':
            break

        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()