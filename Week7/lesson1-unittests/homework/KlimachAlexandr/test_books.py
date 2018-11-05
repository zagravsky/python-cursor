import unittest
from books import Book, Bookshelf
import example


class TestBook(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass: Book')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass: Book')

    def setUp(self):
        print('setUp: Create object\'s')
        self.book_1 = Book('The Hobbit and the Lord of the Rings', 'J.R.R.Tolkien', 2012, 'Fantasy')
        self.book_2 = Book('Indianapolis', 'Lynn Vincent', 2018, 'History')
        self.book_3 = Book('The Outsider', 'Stephen King', 2018, 'Horror')

    def tearDown(self):
        print('tearDown: Clean\n')

    def test_book_title(self):
        print('test_book_title')
        self.assertEqual(self.book_1.book_description, example.b_title_one)
        self.assertEqual(self.book_2.book_description, example.b_title_two)
        self.assertEqual(self.book_3.book_description, example.b_title_three)


class TestBookshelf(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass: BookShelf')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass: BookShelf')

    def setUp(self):
        print('setUp: Create object\'s')
        self.book_1 = Book('The Hobbit and the Lord of the Rings', 'J.R.R.Tolkien', 2012, 'Fantasy')
        self.book_2 = Book('Indianapolis', 'Lynn Vincent', 2018, 'History')
        self.book_3 = Book('The Outsider', 'Stephen King', 2018, 'Horror')

        self.shelf = Bookshelf('Books of the century')

    def tearDown(self):
        print('tearDown: Clean\n')

    def test_add_book(self):
        print('test_add_book')
        self.shelf.add_book(self.book_1)
        self.shelf.add_book(self.book_2)
        self.shelf.add_book(self.book_3)

        self.assertIn(self.book_1, self.shelf.books)
        self.assertIn(self.book_2, self.shelf.books)
        self.assertIn(self.book_3, self.shelf.books)

        self.assertEqual(len(self.shelf.books), 3)

    def test_description(self):
        print('test_description')
        self.shelf.add_book(self.book_1)
        self.shelf.add_book(self.book_2)
        self.shelf.add_book(self.book_3)

        self.assertEqual(self.shelf.description, example.description)

    def test_delete_book(self):
        print('test_delete_book')
        self.shelf.add_book(self.book_1)
        self.shelf.add_book(self.book_2)
        self.shelf.add_book(self.book_3)

        self.shelf.delete_book(self.book_1)
        self.shelf.delete_book(self.book_2)

        self.assertNotIn(self.book_1, self.shelf.books)
        self.assertNotIn(self.book_2, self.shelf.books)
        self.assertIn(self.book_3, self.shelf.books)
        self.assertEqual(len(self.shelf.books), 1)


if __name__ == '__main__':
    unittest.main()
