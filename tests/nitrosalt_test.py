import unittest
import sys
import os
from testing.main_ import *
# у модуля sys є атрибут path - список з усіма директоріями системними і оск це список, то він має метод append
sys.path.append(os.getcwd())


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

# оскільки наш файл (модуль) з кодом main_.py знаходиться на рівень вище, ніж тести,
# то виникає проблема імпортування всіх функцій, сутностей із файлу main_.py у файл test.py
# щоб імпортувати модуль, який знаходиться на рівень вище, потрібно додати папку testing_unittesting у системну змінну path
# і для цього ми імпортуємо ще два модулі: import sys, import os
