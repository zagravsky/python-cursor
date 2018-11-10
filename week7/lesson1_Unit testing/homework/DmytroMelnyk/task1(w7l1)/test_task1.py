import unittest
from task1 import Book, Bookshelf


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book('DARK SACRED NIGHT', 'Michael Connelly')
        self.book2 = Book('ELEVATION', 'Stephen King')
        self.book3 = Book('THE RECKONING', 'John Grisham')

    def test_instance_book(self):
        book1 = Book('DARK SACRED NIGHT', 'Michael Connelly')
        self.assertIsInstance(book1, Book, msg='book1 is not instance of Book')

    def test_book_str_(self):
        self.assertEqual(self.book1.__str__(), 'Book: DARK SACRED NIGHT,\nAuthor: Michael Connelly')
        self.assertEqual(self.book2.__str__(), 'Book: ELEVATION,\nAuthor: Stephen King')
        self.assertEqual(self.book3.__str__(), 'Book: THE RECKONING,\nAuthor: John Grisham')
        self.assertEqual(self.book1.author, 'Michael Connelly')
        self.assertEqual(self.book2.author, 'Stephen King')
        self.assertEqual(self.book3.author, 'John Grisham')


class TestBookshelf(unittest.TestCase):

    def setUp(self):
        self.book1 = Book('DARK SACRED NIGHT', 'Michael Connelly')
        self.book2 = Book('ELEVATION', 'Stephen King')
        self.book3 = Book('THE RECKONING', 'John Grisham')
        self.description = "Books:\n" \
                           "DARK SACRED NIGHT - Michael Connelly\n" \
                           "ELEVATION - Stephen King\n" \
                           "THE RECKONING - John Grisham"

    def test_instance_book_shelf(self):
        self.shelf = Bookshelf("Test bookshelf BestSellers")
        self.assertIsInstance(self.shelf, Bookshelf, msg='shelf is not instance of Bookshelf')

    def test_add_(self):
        shelf = Bookshelf("Test2 bookshelf BestSellers")
        shelf += self.book1
        shelf += self.book2
        shelf += self.book3
        self.assertIsNotNone(shelf)
        self.assertEqual(shelf.description, self.description)


if __name__ == '__main__':
    unittest.main()
