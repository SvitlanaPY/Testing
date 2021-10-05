import unittest
from unittests_testing.nitro_ import *


class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_mass(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(800), 8)

    def test_nitro_salt_returns_integer(self):
        self.assertIsInstance(nitro_salt(1000), int)

    def test_nitro_salt_receives_string_returns_integer(self):
        self.assertEqual(nitro_salt('1000'), 10)

    def test_nitro_salt_receives_alpha_string_returns_zero(self):
        self.assertEqual(nitro_salt("hfghf"), 0)


if __name__ == '__main__':
    unittest.main()
    # метод main() у unittest, який азапускає всі наші тести

# оскільки наш файл (модуль) з кодом nitro_.py знаходиться на рівень вище, ніж тести,
# то виникає проблема імпортування всіх функцій, сутностей із файлу nitro_.py у файл test.py
# щоб імпортувати модуль, який знаходиться на рівень вище, потрібно додати папку testing_unittesting у системну змінну path
# і для цього можна використати два модулі: import sys, import os
