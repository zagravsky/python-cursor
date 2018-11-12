
class Bookshelf:

    books = list()

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def description(self):
        return f'Bookshelf {self.name} heve {len(self)} books'

    def add_book(self, book):
        if len(self.books) < self.size:
            self.books.append(book)
            return self
        else:
            return 'Bookshelf is full '

    def print_books(self):
        for book in self.books:
            print(book)

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f' {len(self)} books on {self.name}'



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.author} --- {self.title}'

