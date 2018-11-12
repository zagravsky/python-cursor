import unittest
from Books import Book, Bookshelf
from unittest import mock
from get_image import get_image



class Bookshelf_Test(unittest.TestCase):


    def setUp(self):

        self.my_shelf = Bookshelf('my_shelf', 10)
        self.book1 = Book('Conan Doyle', 'Sherlock Holmes')
        self.book2 = Book('Jules Gabriel Verne', 'Voyages extraordinaires')

    def test_book(self):
        """testing book create"""
        print("id: " + self.id())
        self.assertTrue(self.book1.__str__() == str('Sherlock Holmes --- Conan Doyle'))

    def test_bookshelf_init(self):
        """test arg initiation"""
        print("id: " + self.id())
        self.assertEqual((self.my_shelf.name, self.my_shelf.size), ('my_shelf', int(10)), 'Wrong Bookshelf!')

    def test_add_book(self):
        """testing add books to bookshelf """
        print("id: " + self.id())
        self.my_shelf.add_book(self.book1)
        self.my_shelf.add_book(self.book2)
        self.assertEqual(len(self.my_shelf),  2)

    def test_description(self):
        """testing bookshelt deskription"""
        print("id: " + self.id())
        self.assertTrue(self.my_shelf.description() == 'Bookshelf my_shelf heve 2 books')


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

    @mock.patch('get_image.rq.get', side_effect=mocked_requests_get)
    def test_requests(self, mock_get):
        """test download image"""
        print("id: " + self.id())
        self.assertEqual(get_image(), b'picture')


if __name__ == '__main__':
    unittest.main()