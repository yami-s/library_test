import json
from book import Book

class Library:
    def __init__(self, data_file='data.json'):
        self.data_file = data_file
        self.books = self.load_data()

    def load_data(self) -> list:
        try:
            with open(self.data_file, 'r') as file:
                books_data = json.load(file)
            return [Book(**book) for book in books_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)

    def add_book(self, title: str, author: str, year: int):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year, 'в наличии')
        self.books.append(new_book)
        self.save_data()
        print("Книга добавлена.")

    def remove_book(self, book_id: int):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_data()
                print("Книга удалена.")
                return
        print("Книга с таким ID не найдена.")

    def search_book(self, query: str):
        results = [book for book in self.books if query.lower() in book.title.lower() or 
                   query.lower() in book.author.lower() or str(book.year) == query]
        if results:
            for book in results:
                print(book)
        else:
            print("Книги не найдены.")

    def display_books(self):
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(book)

    def change_status(self, book_id: int, new_status: str):
        if new_status not in ['в наличии', 'выдана']:
            print("Недопустимый статус. Пожалуйста, укажите 'в наличии' или 'выдана'.")
            return
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_data()
                print("Статус книги изменён.")
                return
        print("Книга с таким ID не найдена.")