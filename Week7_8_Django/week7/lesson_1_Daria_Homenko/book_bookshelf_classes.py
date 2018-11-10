class Bookshelf:

    list_of_books = []

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def __add__(self, book):
        if len(self.list_of_books) < self.volume:
            self.list_of_books.append(book)
            return self
        else:
            return 'Bookshelf is full '

    def bookshelf_description(self):
        return f'{self.name} bookshelf designed for {self.volume} books'


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def about(self):
        return "'{}' was written by {}".format(self.title, self.author)

    def __str__(self):
        return '{} - {}'.format(self.title, self.author)
