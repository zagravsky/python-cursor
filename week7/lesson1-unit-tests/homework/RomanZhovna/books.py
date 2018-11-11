class BookShelf:

    def __init__(self, shelf_number: str):
        self.shelf_number = shelf_number
        self.booklist = list()

    def __add__(self, book: object):
        self.booklist.append(book)
        return self

    def description(self):
        return f"{self.shelf_number}:\n" + '\n'.join([book.printbook for book in self.booklist])


class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    @property
    def printbook (self):
        return f"Title: {self.title}, Author: {self.author}"
