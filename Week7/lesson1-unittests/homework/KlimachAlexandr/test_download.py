import unittest
from unittest.mock import patch
from download_something import download_something


class Download(unittest.TestCase):
    def test_download_something(self):
        with patch('requests.get') as mock_request:
            url = 'http://local.host'
            mock_request.return_value.content = b'picture'
            mock_request.response = download_something(url)
            self.assertIsNotNone(mock_request.response)
            self.assertEqual(mock_request.response, b'picture')
            self.assertNotEqual(mock_request.response, b'blah')
