import unittest

from class_book import Book, BookShelf


class TestBookClass(unittest.TestCase):

    def setUp(self):
        self.book1 = Book('Inferno', 'Dan Brown', 2013)
        self.book2 = Book('A briefer history of time', 'Stephen Hawking', 2005)

    def tearDown(self):
        pass

    def test_book(self):
        self.assertIsNotNone(Book)
        self.assertIsInstance(self.book1, Book)
        self.assertIsInstance(self.book2, Book)

    def test_description(self):
        self.assertEqual(self.book1.description, "'Inferno', Dan Brown (2013)")
        self.assertEqual(self.book2.description, "'A briefer history of time', Stephen Hawking (2005)")


class TestBookshelfClass(unittest.TestCase):

    def setUp(self):
        self.book1 = Book('Inferno', 'Dan Brown', 2013)
        self.book2 = Book('A briefer history of time', 'Stephen Hawking', 2005)
        self.shelf_with_books = BookShelf()

    def tearDown(self):
        del self.shelf_with_books.list_of_books[:]

    def test_bookshelf(self):
        self.assertIsInstance(self.shelf_with_books, BookShelf)

    def test_append_book(self):
        self.shelf_with_books.append_book(self.book1)
        self.shelf_with_books.append_book(self.book2)

        self.assertIn(self.book1, self.shelf_with_books.list_of_books)
        self.assertIn(self.book2, self.shelf_with_books.list_of_books)

    def test_description(self):
        self.shelf_with_books.append_book(self.book1)
        self.assertEqual(self.shelf_with_books.description, "1. 'Inferno', Dan Brown")

        self.shelf_with_books.append_book(self.book2)
        self.assertEqual(self.shelf_with_books.description, "1. 'Inferno', Dan Brown\n"
                                                            "2. 'A briefer history of time', Stephen Hawking")


if __name__ == '__main__':
    unittest.main()
