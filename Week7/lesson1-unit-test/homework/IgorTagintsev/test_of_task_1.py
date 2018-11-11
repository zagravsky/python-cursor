import unittest
from task_1 import Book, Bookshelf


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book('In Search of Lost Time', 'Marcel Proust')
        self.book2 = Book('Don Quixote', 'Miguel de Cervantes')
        self.book3 = Book('The Great Gatsby', 'Scott Fitzgerald')

    def test_instance_book(self):
        book1 = Book('In Search of Lost Time', 'Marcel Proust')
        self.assertIsInstance(book1, Book, msg='book1 is not instance of Book')

    def test_book_str_(self):
        self.assertEqual(self.book1.__str__(), 'Book: In Search of Lost Time,\nAuthor: Marcel Proust')
        self.assertEqual(self.book2.__str__(), 'Book: Don Quixote,\nAuthor: Miguel de Cervantes')
        self.assertEqual(self.book3.__str__(), 'Book: The Great Gatsby,\nAuthor: Scott Fitzgerald')
        self.assertEqual(self.book1.author, 'Marcel Proust')
        self.assertEqual(self.book2.author, 'Miguel de Cervantes')
        self.assertEqual(self.book3.author, 'Scott Fitzgerald')


class TestBookshelf(unittest.TestCase):
    def setUp(self):
        self.book1 = Book('In Search of Lost Time', 'Marcel Proust')
        self.book2 = Book('Don Quixote', 'Miguel de Cervantes')
        self.book3 = Book('The Great Gatsby', 'Scott Fitzgerald')
        self.description = "Books:\n" \
                           "In Search of Lost Time - Marcel Proust\n" \
                           "Don Quixote - Miguel de Cervantes\n" \
                           "The Great Gatsby - Scott Fitzgerald"

    def test_instance_book_shelf(self):
        self.shelf = Bookshelf("Test bookshelf TheGreatestBooks")
        self.assertIsInstance(self.shelf, Bookshelf, msg='shelf is not instance of Bookshelf')

    def test_add_(self):
        shelf = Bookshelf("Test2 bookshelf TheGreatestBooks")
        shelf += self.book1
        shelf += self.book2
        shelf += self.book3
        self.assertIsNotNone(shelf)
        self.assertEqual(shelf.description, self.description)


if __name__ == '__main__':
    unittest.main()