from unittest import TestCase, mock

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
    @mock.patch('get_data.requests.get')
    def test_data_downloader(self, mock_get):
        mock_get.return_value.content = b'picture'
        response = get_data('')

        self.assertEqual(response.content, b'picture')
