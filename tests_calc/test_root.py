import unittest
from Testing.calc_ import Calc


class TestRoot(unittest.TestCase):
    """
    Testing square root of any number in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Sqrt_DataInputs(self):
        print('test_Sqrt_DataInputs')
        self.assertIsInstance(Calc.root(4), float)
        self.assertIsInstance(Calc.root(9.0), float)

    def test_Sqrt_Computing(self):
        print('test_Sqrt_Computing')
        self.assertEqual(Calc.root(0.0), 0)
        self.assertEqual(Calc.root(625), 25.0)
        self.assertEqual(Calc.root(4.0), 2.0)

    def test_Sqrt_RaiseExceptions(self):
        print('test_Sqrt_RaiseExceptions')
        # self.assertRaises(ValueError, Calc.root, -25)
        with self.assertRaises(ValueError):
            Calc.root(-25)
        # self.assertRaises(TypeError, Calc.root, "4")
        with self.assertRaises(TypeError):
            Calc.root("25")

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()
