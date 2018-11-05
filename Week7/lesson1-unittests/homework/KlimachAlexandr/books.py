class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    @property
    def book_description(self):
        return f"Book: {self.title}\n" \
               f"Author: {self.author}\n" \
               f"Year: {self.year}\n" \
               f"Genre: {self.genre}\n"


class Bookshelf:
    def __init__(self, shelf_name):
        self.shelf_name = shelf_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    @property
    def description(self):
        return '\n'.join([book.book_description for book in self.books])

    def delete_book(self, book):
        if book in self.books:
            self.books.remove(book)