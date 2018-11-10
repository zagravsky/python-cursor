import unittest
from book_bookshelf_classes import Book, Bookshelf
from unittest import mock
import download_image


class Bookshelf_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('{:*^50}'.format('Bookshelf_Test'))

    @classmethod
    def tearDownClass(cls):
        print('{:=^50}'.format('end'), end='\n\n')

    def setUp(self):
        print("Set up for [" + self.shortDescription() + "]")
        self.Blue_shelf = Bookshelf('Blue', 5)
        self.book_1 = Book('Hamlet', 'William Shakespeare')
        self.book_2 = Book('Moby Dick', 'Herman Melville')
        self.book_3 = Book('War', 'Leo Tolstoy')

    def tearDown(self):
        print("Tear down[" + self.shortDescription() + "]")
        print(" ")

    def test_bookshelf_init(self):
        """test arg initiation"""
        print("id: " + self.id())
        self.assertEqual((self.Blue_shelf.name, self.Blue_shelf.volume), (str('Blue'), int(5)), 'Wrong args!')

    def test_bookshelf_description(self):
        """testing description operation"""
        print("id: " + self.id())
        self.assertTrue(Bookshelf.bookshelf_description(self.Blue_shelf) == 'Blue bookshelf designed for 5 books',
                        'Wrong screen output!')

    def test_add(self):
        """testing add books to bookshelf operation"""
        print("id: " + self.id())
        self.Blue_shelf += self.book_1
        self.Blue_shelf += self.book_2
        self.Blue_shelf += self.book_3
        self. assertEqual(len(self.Blue_shelf.list_of_books), 3, 'Books was not correct added to bookshelf')

    def test_book_instance(self):
        """testing instance operation"""
        print("id: " + self.id())
        self.assertIsInstance(self.Blue_shelf, Bookshelf, 'Blue_shelf is not instance of Bookshelf classes')


class Book_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('{:*^50}'.format('Book_Test'))

    @classmethod
    def tearDownClass(cls):
        print('{:=^50}'.format('end'), end='\n\n')

    def setUp(self):
        print("Set up for [" + self.shortDescription() + "]")

        self.book_1 = Book('Hamlet', 'William Shakespeare')
        self.book_2 = Book('Moby Dick', 'Herman Melville')
        self.book_3 = Book('War and peace', 'Leo Tolstoy')

    def tearDown(self):
        print("Tear down[" + self.shortDescription() + "]")
        print(" ")

    def test_init(self):
        """test arg initiation"""
        print("id: " + self.id())

        self.assertEqual((self.book_1.title, self.book_1.author), (str('Hamlet'), str('William Shakespeare')))

    def test_book_str(self):
        """test print books operation"""
        print("id: " + self.id())
        self.assertTrue(str(self.book_1) == "Hamlet - William Shakespeare")

    def test_book_about(self):
        """test books_about operation"""
        print("id: " + self.id())
        self.assertTrue(Book.about(self.book_3) == "'War and peace' was written by Leo Tolstoy")


class Image_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('{:*^50}'.format('Image_Test'))

    @classmethod
    def tearDownClass(cls):
        print('{:=^50}'.format('end'), end='\n\n')

    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, content, status_code):
                self.content = content
                self.status = status_code

            def content(self):
                return self.content

        return MockResponse(b'picture', 200)

    @mock.patch('download_image.rq.get', side_effect=mocked_requests_get)
    def test_requests(self, mock_get):
        """test download image"""
        print("id: " + self.id())
        self.assertEqual(download_image.get_image(), b'picture')


if __name__ == '__main__':
    unittest.main()
