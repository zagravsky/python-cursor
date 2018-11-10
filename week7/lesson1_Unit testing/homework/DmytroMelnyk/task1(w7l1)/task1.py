# Task 1
#
# Create classes Book and Bookshelf with any fields you want.
# The only condition is - Bookshelf should contain the Book instances.
# Add description property to the Bookshelf class, which should be formatted, using f{}.
# Test creation and properties of both classes using unittest.


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title},\nAuthor: {self.author}"


class Bookshelf:
    book_shelf = []

    def __init__(self, book):
        self.book = book

    def __add__(self, book):
        self.book_shelf.append(book)
        return self

    @property
    def description(self):
        return 'Books:\n'+'\n'.join([f'{book.title} - {book.author}' for book in self.book_shelf])


if __name__ == '__main__':
    book1 = Book('DARK SACRED NIGHT', 'Michael Connelly')
    book2 = Book('ELEVATION', 'Stephen King')
    book3 = Book('THE RECKONING', 'John Grisham')
    print(book1)
    print(book2)
    print(book3)
    print(book1.author)
    shelf = Bookshelf('BestSellers')
    shelf += book1
    shelf += book2
    shelf += book3
    print(shelf.description)
