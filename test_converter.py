import unittest
from converter import convert_currency

class TestConverter(unittest.TestCase):
    def test_usd(self):
        # Проверяем, что 100 баксов конвертятся в успех
        res = convert_currency(100, "USD")
        self.assertEqual(res["status"], "success")

    def test_negative(self):
        # Проверяем, что на -10 прилетит ошибка
        res = convert_currency(-10, "EUR")
        self.assertEqual(res["status"], "error")