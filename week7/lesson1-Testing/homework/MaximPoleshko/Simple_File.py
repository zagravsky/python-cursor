class Book():
    name = None
    year = None
    price = None
    complexity = None

    def __init__(self, name:str, year:int, complexity:str, price:int):
        self.name = name
        self.year = year
        self.complexity = complexity
        self.price = price

    def __str__(self):
        return f'Book: {self.name}, Year: {self.year}, Complexity: {self.complexity}'

first_book = Book('Learn Python the Hard Way', 2013, 'for beginner', 99)
second_book = Book('Python Practice Book', 2016, 'for beginner', 44)
print(first_book)
print(second_book)


class BookShelf():
    books_list = []

    def __init__(self, book):
        self.book = book

    def __add__(self, book: Book):
        self.books_list.append(book)
        return self

    @property
    def description(self):
        return '\nDescription:\n'+'\n'.join([f'\tName: {book.name}, Price: {book.price}' for book in self.books_list])

shelf = BookShelf('shelf')
shelf += first_book
shelf += second_book
print(shelf.description)