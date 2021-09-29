import unittest
from testing.calc_ import Calc


class TestMult(unittest.TestCase):
    """
    TESTing_ multiplication of values in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Multiply_DataInputs(self):
        print('test_Multiply_DataInputs')
        self.assertIsInstance(Calc.mul(1, 2), int)
        self.assertIsInstance(Calc.mul(2.0, 2), float)
        self.assertIsInstance(Calc.mul(2, 3.0), float)

    def test_Multiply_Computing(self):
        print('test_Multiply_Computing')
        self.assertEqual(Calc.mul(0.0, 0), 0)
        self.assertEqual(Calc.mul(100, 2), 200.0)
        self.assertEqual(Calc.mul(-5, 2), -10)
        self.assertEqual(Calc.mul(10, 5.0), 50)

    def test_Multiply_SpecialCase(self):
        print('test_Multiply_SpecialCase')
        self.assertEqual(Calc.mul(3, '500'), '500500500')

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()

# if there is unittest.main() in a python-file then run command ~$ python3 HW#11_UnitTests.py
# or
# if there is no unittest.main() in a python-file,
# then run command ~$ python3 -m unittest -v HW#11_UnitTests.py > output_unittesting.txt
# testing_unittesting results will be saved in file 'output_unittesting.txt'
