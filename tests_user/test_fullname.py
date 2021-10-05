from unittests_testing.user_ import User
import unittest

class TestUser(unittest.TestCase):
    def test_fullname(self):
        user_1 = User("Anna", "Popivchak", 33)

        user_1.set_full_name("Petrov Petr")

        self.assertEqual(user_1.name, "Petr")
        self.assertEqual(user_1.surname, "Petrov")
