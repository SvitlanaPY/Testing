import unittest
from unittests_testing.calc_ import Calc


class TestPow(unittest.TestCase):
    """
    Testing rise any number to the power in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Power_DataInputs(self):
        print('test_Power_DataInputs')
        self.assertIsInstance(Calc.pow(4, 2), int)
        self.assertIsInstance(Calc.pow(2.0, 2), float)
        self.assertIsInstance(Calc.pow(50, 2.0), float)

    def test_Power_Computing(self):
        print('test_Power_Computing')
        self.assertEqual(Calc.pow(0.0, 0), 1)
        self.assertEqual(Calc.pow(0, 1), 0.0)
        self.assertEqual(Calc.pow(-5, 11), -48828125)
        self.assertEqual(Calc.pow(-5.0, 2), 25)

    def test_Power_RaiseExceptions(self):
        print('test_Power_RaiseExceptions')
        # self.assertRaises(TypeError, Calc.pow, "10", 2)
        with self.assertRaises(TypeError):
            Calc.pow("10", 2)

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()
