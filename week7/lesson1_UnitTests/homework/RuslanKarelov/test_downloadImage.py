from unittest.mock import patch
from unittest import TestCase

from download_image import image


class TestDownloadImage(TestCase):

    def test_image(self):
        with patch('download_image.requests.get') as mocked_get:
            mocked_get.return_value.content = b'picture'

            url = 'https://some.url'
            result = image(url)
            self.assertEqual(result, b'picture')
