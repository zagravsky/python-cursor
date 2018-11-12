from Task1 import Book, Bookshelf
from unittest import mock, main, TestCase
from io import StringIO

if __name__ == '__main__':
    main(verbosity=2)


class BookTest(TestCase):
    def test_happypath(self):
        """Happy path - create Book class instance with correct info; check the output of 'about' property"""
        test_book1 = Book('HPMOR', 'Yudkowsky', 2015)
        self.assertIsInstance(test_book1, Book)
        self.assertEqual(test_book1.about, 'HPMOR - written by Yudkowsky in 2015')
        del test_book1

    def test_accept_wrong_data_types(self):
        """check whether warning message is shown if arguments with wrong data types are used when creating
        Book instance"""
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_output:
            test_book1 = Book(['HPMOR'], 1337, '2015')
            expected = 'wrong data type for title!\nwrong data type for author!\nwrong data type for year!\n'
            self.assertEqual(mock_output.getvalue(), expected)
            del test_book1

    def test_lacking_arguments(self):
        """check what happens if some attributes are not filled with data """
        with self.assertRaises(TypeError):
            test_book1 = Book('HPMOR', 'Yudkowsky')
            del test_book1


class BookshelfTest(TestCase):
    def setUp(self):
        self.test_book1 = Book('HPMOR', 'Yudkowsky', 2015)
        self.test_book2 = Book('On the Origin of Species', 'Darwin', 1859)
        self.test_shelf1 = Bookshelf(1)

    def test_happypath(self):
        """create Bookshelf instance; create and add two books instances to this Bookshelf instance;
        check the work of Bookshelf instance's description property"""
        self.assertIsInstance(self.test_shelf1, Bookshelf)
        self.test_shelf1.add(self.test_book1, self.test_book2)
        self.assertEqual(self.test_shelf1.description, "Shelf #1. Content - ['HPMOR', 'On the Origin of Species']")

    def test_add_wrong_arguments(self):
        """check whether Bookshelf instance's add() method accepts only Book instances and shows warning message when
        not Book instance is used as an argument"""
        dummy = mock.MagicMock
        wrong_arguments = [1, "two", ['three'], {4: 'five'}, ('six', 7), 89.99, dummy, True]
        for argument in wrong_arguments:
            self.assertEqual(self.test_shelf1.add(argument), f"{argument} is not an instance of Book class")

    def tearDown(self):
        del self.test_book1
        del self.test_book2
        del self.test_shelf1

