class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year


class Bookshelf:
    def __init__(self, *books):
        self.books = books

    @property
    def description(self):
        return "This shelf holds these books:\n" + \
               '\n'.join([f'{book.title} - {book.author}, {book.year}' for book in self.books])


if __name__ == '__main__':
    book1 = Book("Fahrenheit 451", "Ray Bradbury", "1953")
    book2 = Book("Hard to Be a God", "Arkady and Boris Strugatsky", "1964")
    book3 = Book("The Ultimate Hitchhiker's Guide", "Douglas Adams", "1979")

    bookshelf = Bookshelf(book1, book2, book3)
    print(bookshelf.description)
