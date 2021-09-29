import unittest
import sys, os

# у модуля sys є атрибут path - список з усіма директоріями системними і оск це список, то він має метод append

sys.path.append(os.getcwd())
from main import *



class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_integer(self):
        self.assertEqual(nitro_salt(1000), 10)


if __name__ == "__main__":
    unittest.main()
    # метод main() у unittest, який азапускає всі наші тести

# оскільки наш файл (модуль) з кодом main_.py знаходиться на рівень вище, ніж тести,
# то виникає проблема імпортування всіх функцій, сутностей із файлу main_.py у файл test.py
# щоб імпортувати модуль, який знаходиться на рівень вище, потрібно додати папку testing у системну змінну path
# і для цього ми імпортуємо ще два модулі: import sys, import os
