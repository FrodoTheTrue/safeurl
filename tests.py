from unittest import TestCase
from safeurl.core import decodeURL


class MainTestCase(TestCase):
    def test_decodeUrl(self):
        self.assertEqual(decodeURL('http://bit.ly/1gaiW96'),
                         'https://www.yandex.ru/')

    def test_decodeUrlArray(self):
        self.assertEqual(
            decodeURL(['http://bit.ly/1gaiW96', 'http://bit.ly/1gaiW96']),
            ['https://www.yandex.ru/', 'https://www.yandex.ru/'])
