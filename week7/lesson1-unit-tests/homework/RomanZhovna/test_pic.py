import unittest
from unittest.mock import patch
from lesson1.pic import get_pic


class TestPic(unittest.TestCase):

    def test_get_pic(self):
        with patch('requests.get') as mock_request:
            url = 'https://via.placeholder.com/300x300.png'
            mock_request.return_value.content = b'picture'
            mock_request.response.content = get_pic(url)
            self.assertIsNotNone(mock_request.response.content)
            self.assertEqual(mock_request.response.content, b'picture')
