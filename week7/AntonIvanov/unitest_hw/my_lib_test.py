import unittest
from unittest import TestCase, mock
import my_lib as ml


class BookTest(TestCase):
    def setUp(self):
        self.title = "title"
        self.author = "author"

    def test_creation(self):
        class_instance = ml.Book(self.title, self.author)
        self.assertIsNotNone(class_instance)
        self.assertEqual(class_instance.title, self.title)
        self.assertEqual(class_instance.author, self.author)


class BookShelfTest(TestCase):
    def setUp(self):
        self.book_desc = '0. title - author'
        self.book_inst = ml.Book('title', 'author')
        self.class_instance = ml.BookShelf()
        self.class_instance += self.book_inst

    def test_creation(self):
        self.assertIsNotNone(self.class_instance)
        self.assertEqual(self.class_instance.description, self.book_desc)

    def test_take_book(self):
        self.assertEqual(self.class_instance.take_book(1), self.book_inst)



if __name__ == '__main__':
    unittest.main()