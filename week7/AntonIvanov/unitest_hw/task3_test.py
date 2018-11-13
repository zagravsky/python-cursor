from unittest import TestCase
from unittest.mock import patch
from task3 import get_image

class Task3Test(TestCase):
    def test_get_image(self):
        with patch('requests.get') as mocked_request:
            url = 'htttps://url.com'
            content = b'picture'
            mocked_request.return_value.status_code = 200
            mocked_request.return_value.content = content
            response = get_image(url)
            self.assertEqual(response, 200)
            mocked_request.assert_called_once_with(url)