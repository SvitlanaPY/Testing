import unittest
# import sys
# import os

from testing.calc_ import Calc
# sys.path.append(os.getcwd())


class TestMinus(unittest.TestCase):
    """
    TESTing_ subtraction of values in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Subtract_DataInputs(self):
        print('test_Subtract_DataInputs')
        self.assertIsInstance(Calc.minus(1, 2), int)
        self.assertIsInstance(Calc.minus(2.0, 2), float)
        self.assertIsInstance(Calc.minus(2, 3.0), float)

    def test_Subtract_Computing(self):
        print('test_Subtract_Computing')
        self.assertEqual(Calc.minus(0.0, 0), 0)
        self.assertEqual(Calc.minus(-5, -5), 0.0)
        self.assertEqual(Calc.minus(-5, 2), -7)
        self.assertEqual(Calc.minus(10, 5.0), 5)

    def test_Subtract_RaiseExceptions(self):
        print('test_Subtract_RaiseExceptions')
        # self.assertRaises(TypeError, Calc.minus, 52, "2")
        with self.assertRaises(TypeError):
            Calc.minus(52, "2")

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()

# if there is unittest.main() in a python-file then run command ~$ python3 HW#11_UnitTests.py
# or
# if there is no unittest.main() in a python-file,
# then run command ~$ python3 -m unittest -v HW#11_UnitTests.py > output_unittesting.txt
# testing_unittesting results will be saved in file 'output_unittesting.txt'
