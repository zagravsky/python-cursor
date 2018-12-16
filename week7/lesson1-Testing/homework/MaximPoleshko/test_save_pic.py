from save_pic import save_img
from unittest import TestCase
from unittest.mock import patch

class TestDownloadPicture(TestCase):
    def test_save_pic(self):
        with patch('requests.get') as mock_test:

            url = 'https://dummyimage.com/600x400/000/fff'
            mock_test.return_value.content = b'picture'
            mock_test.response.content = save_img(url)

            self.assertIsNotNone(mock_test.response.content)
            self.assertEqual(mock_test.response.content, b'picture')
