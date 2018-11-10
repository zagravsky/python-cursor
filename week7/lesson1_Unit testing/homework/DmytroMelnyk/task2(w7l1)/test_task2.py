import unittest
from unittest.mock import patch

from task2 import dowlnoad_from_url


class Test_download_from_url(unittest.TestCase):

    def test_dowlnoad_from_url(self):
        with patch('requests.get') as mock_request:
            url = 'https://dummyimage.com/600x400/000/fff'
            mock_request.return_value.content = b'picture'
            mock_request.response = dowlnoad_from_url(url)
            self.assertIsNotNone(mock_request.response)
            self.assertEqual(mock_request.response, b'picture')


if __name__ == '__main__':
    unittest.main()


