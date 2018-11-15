class Book:

    def __init__(self, name: str, author: str, year_of_publish: int):
        self.name = name
        self.author = author
        self.year_of_publish = year_of_publish

    @property
    def description(self) ->str:
        return f"'{self.name}', {self.author} ({self.year_of_publish})"


class BookShelf:
    list_of_books = []

    def append_book(self, book) ->list:
        self.list_of_books.append(book)
        return self.list_of_books

    @property
    def description(self) ->str:
        desc_of_shelf = []
        for num, book in enumerate(self.list_of_books):
            num += 1
            desc_of_shelf += [f"{num}. '{book.name}', {book.author}"]
        n = "\n"
        return f"{n.join(desc_of_shelf)}"


if __name__ == "__main__":

    book1 = Book("Doom", "Jack London", 2000)
    print(book1.description)
    bookShelf = BookShelf()
    bookShelf.append_book(book1)

    #book2 = Book("Azaz", "Marc Rufalo", 1994)
    #bookShelf.append_book(book2)
    print(bookShelf.description)
    print(bookShelf.list_of_books)
