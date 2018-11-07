from unittest import TestCase
from unittest.mock import patch

from library import Book, Bookshelf
from data_downloader import get_data


class TestBook(TestCase):

    def setUp(self):
        self.title = 'Fahrenheit 451'
        self.author = 'Ray Bradbury'
        self.year = '1953'

    def test_book(self):
        book = Book(self.title, self.author, self.year)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, self.title)
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.year, self.year)


class TestBookshelf(TestCase):

    def setUp(self):
        self.book1 = Book("Fahrenheit 451", "Ray Bradbury", "1953")
        self.book2 = Book("Hard to Be a God", "Arkady and Boris Strugatsky", "1964")
        self.book3 = Book("The Ultimate Hitchhiker's Guide", "Douglas Adams", "1979")
        self.description = "This shelf holds these books:\n" \
                           "Fahrenheit 451 - Ray Bradbury, 1953\n" \
                           "Hard to Be a God - Arkady and Boris Strugatsky, 1964\n" \
                           "The Ultimate Hitchhiker's Guide - Douglas Adams, 1979"

    def test_bookshelf(self):
        bookshelf = Bookshelf(self.book1, self.book2, self.book3)
        self.assertIsNotNone(bookshelf)
        self.assertEqual(bookshelf.description, self.description)


class TestDataDownloader(TestCase):

    @patch('data_downloader.requests.get')
    def test_data_downloader(self, mocked_get):
        mocked_get.return_value.content = b'picture'
        response = get_data('https://test.page')
        mocked_get.assert_called_with('https://test.page')
        self.assertEqual(response.content, b'picture')


if __name__ == '__main__':
    from unittest import main

    main()
