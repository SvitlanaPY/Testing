from unittests_testing.user_ import User
import unittest

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user_1 = User("Anna", "Polishchuk", 33)
        self.user_2 = User("Sofiya", "Popivchak", 12)

    def test_fullname(self):
        self.user_1.set_full_name("Petrov Petr")
        self.assertEqual(self.user_1.name, "Petr")
        self.assertEqual(self.user_1.surname, "Petrov")

        self.user_2.set_full_name("Ivanov Ivan")
        self.assertEqual(self.user_2.name, "Ivan")
        self.assertEqual(self.user_2.surname, "Ivanov")


    def tearDown(self) -> None:
        pass