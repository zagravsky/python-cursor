import unittest
from unittest import TestCase, mock

import Simple_File as sf
from Simple_File import Book, BookShelf

class TDDTest(TestCase):
    def setUp(self):
        self.name = "Learn Python the Hard Way"
        self.year = 2013
        self.complexity = "for beginner"
        self.price = 99

    def test_creation(self):
        class_instance = sf.Book(self.name, self.year, self.complexity, self.price)
        self.assertIsNotNone(class_instance)
        self.assertEqual(class_instance.name, self.name)
        self.assertEqual(class_instance.year, self.year)
        self.assertEqual(class_instance.complexity, self.complexity)
        self.assertEqual(class_instance.price, self.price)

    def book_return(self):
        class_instance = sf.Book(self.name, self.year, self.complexity, self.price)
        self.assertEqual(f'{class_instance.name}, {class_instance.price}, {class_instance.complexity}, {class_instance.year}')

class BookShelfTest(TestCase):
    def setUp(self):
        self.shelf_name = 'book_shelf_first'
        self.first_book = Book('Learn Python the Hard Way', 2013, 'for beginner', 99)
        self.second_book = Book('Python Practice Book', 2016, 'for beginner', 44)
        self.shelf = sf.BookShelf('shelf_1')

    def book_shelf_test_creation(self):
        class_instance = sf.BookShelf(self.shelf_name)
        self.assertIsNotNone(class_instance)
        self.assertEqual(class_instance.shelf_name, self.shelf_name)

    def test_add_(self):
        shelf = BookShelf("book_shelf_Test2")
        shelf += self.first_book
        shelf += self.second_book
        self.assertIsNotNone(shelf)

if __name__ == '__main__':
    unittest.main()