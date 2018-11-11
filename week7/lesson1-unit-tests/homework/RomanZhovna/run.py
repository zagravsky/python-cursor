from lesson1.books import BookShelf, Book


if __name__ == "__main__":
    shelf = BookShelf('Shelf #1')

    # print(shell_1.description())

    book_1 = Book("Memoirs of a Geisha", "Arthur Golden")
    book_2 = Book("A Game of Thrones", "George R.R. Martin")
    book_3 = Book("Great Expectations", "Charles Dickens")

    shelf += book_1
    shelf += book_2
    shelf += book_3

    print(book_1.author)
    print(shelf.description())
