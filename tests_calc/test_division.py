import unittest
from Testing.calc_ import Calc

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

# якщо у модулі є блок:
# if __name__ == '__main__':
#     unittest.main()
# то наш модуль test_division.py можна запустити в терміналі напряму, командою: ~$ python3 test_division.py
# ця команда рівносильна запуску тестів через меню Run, це запуск модуля самостійно, а НЕ як імпортованого модуля
# (при такому запуску if __name__ == '__main__' і функція main() у unittest запустить наш файл test_division.py з тестами як окремий модуль напряму)
# or
# запускаючи тести командою ~$ python3 -m unittest -v test_division.py > output_unittesting.txt
# ми вказуємо інтерпретатору пайтон запустити наш модуль test_division.py з тестами з бібліотеки unittest як імпортованого модуля
# ця команда - це скорочення для командної стрічки для запуску метода main() з бібліотеки unittest;
# при такому запуску наш модуль втрачає імя "main", а набуває імені модуля: __name__ == "test_division",
# оск він імпортується і запускається з бібліотеки unittest, і блок if ... не буде виконуватись:
# if __name__ == '__main__':
#     unittest.main()
# тепер сама бібліотека unittest буде знати, що робити і як запустити імпортований модуль;
# results will be saved in file 'output_unittesting.txt'
