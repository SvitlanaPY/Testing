import unittest
from unittests_testing.calc_ import Calc


class TestDiv(unittest.TestCase):
    """
    Testing division of values in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Divide_DataInputs(self):
        print('test_Divide_DataInputs')
        self.assertIsInstance(Calc.div(4, 2), float)
        self.assertIsInstance(Calc.div(2.0, 2), float)
        self.assertIsInstance(Calc.div(50, 2.0), float)

    def test_Divide_Computing(self):
        print('test_Divide_Computing')
        self.assertEqual(Calc.mul(0.0, 1), 1)
        self.assertEqual(Calc.div(100, 2.0), 50)
        self.assertEqual(Calc.div(-50, 2), -25)
        self.assertEqual(Calc.div(-5, -5), 1.0)

    def test_Division_RaiseExceptions(self):
        print('test_Division_RaiseExceptions')
        # self.assertRaises(ZeroDivisionError, Calc.div, 10, 0)
        with self.assertRaises(ZeroDivisionError):
            Calc.div(10, 0)
        # self.assertRaises(TypeError, Calc.div, 52, "2")
        with self.assertRaises(TypeError):
            Calc.div(52, "2")

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()

# if there is unittest.main() in a python-file then run command:
# ~$ python3 test_division.py
# (функція main() у unittest запустить наш файл test_division.py з тестами як окремий модуль напряму:
# і наш модуль буде мати імя "main": __name__ == '__main__'
# or
# command ~$ python3 -m unittest -v test_division.py > output_unittesting.txt
# ми вказуємо інтерпретатору пайтон запустити наш модуль test_division.py з тестами з бібліотеки unittest як імпортованого модуля
# тобто тепер наш модуль втрачає імя "main", а набуває імені модуля: __name__ == "test_division",
# оск він імпортується і запускається з бібліотеки unittest.

# results will be saved in file 'output_unittesting.txt'
