import unittest
from lesson1.books import Book, BookShelf


class TestBook(unittest.TestCase):
    """setUp runs before each single test"""
    def setUp(self):
        self.book_1 = Book("Memoirs of a Geisha", "Arthur Golden")

    def test_book(self):
        self.assertEqual(f"{self.book_1.title}, {self.book_1.author}", "Memoirs of a Geisha, Arthur Golden")

    def test_printbook(self):
        self.assertEqual(self.book_1.printbook, "Title: Memoirs of a Geisha, Author: Arthur Golden")


class TestBookShell(unittest.TestCase):
    """setUp runs before each single test"""
    def setUp(self):
        self.shelf = BookShelf("Shelf #1")
        self.book_1 = Book("Memoirs of a Geisha", "Arthur Golden")
        self.book_2 = Book("A Game of Thrones", "George R.R. Martin")
        self.book_3 = Book("Great Expectations", "Charles Dickens")
        self.shelf += self.book_1
        self.shelf += self.book_2
        self.description = "Shelf #1:\n" \
                           "Title: Memoirs of a Geisha, Author: Arthur Golden\n" \
                           "Title: A Game of Thrones, Author: George R.R. Martin"

    def test_shelf(self):
        self.assertIsNotNone(self.shelf.booklist)
        self.assertIn(self.book_1, self.shelf.booklist)
        self.assertIn(self.book_2, self.shelf.booklist)
        self.assertNotIn(self.book_3, self.shelf.booklist)

    def test_description(self):
        self.assertEqual(self.description, self.shelf.description())


if __name__ == "__main__":
    unittest.main()()
