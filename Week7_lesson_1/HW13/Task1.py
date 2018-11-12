class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title if type(title) == str else print('wrong data type for title!')
        self.author = author if type(author) == str else print('wrong data type for author!')
        self.year = year if type(year) == int else print('wrong data type for year!')

    @property
    def about(self):
        """Get info about the book"""
        return f"{self.title} - written by {self.author} in {self.year}"


class Bookshelf:
    def __init__(self, number: int):
        self.number = number
        self.books_on_shelf = []   # as per https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

    def add(self, *books):
        for book in books:
            if isinstance(book, Book):
                self.books_on_shelf.append(book)
            else:
                return f"{book} is not an instance of Book class"

    @property
    def description(self):
        """Get description of the bookshelf"""
        book_names = [book.title for book in self.books_on_shelf]
        return f"Shelf #{self.number}. Content - {book_names}"


b1 = Book('HPMOR', 'Yudkowsky', 2015)
b2 = Book('On the Origin of Species', 'Darwin', 1859)

sh1 = Bookshelf(1)