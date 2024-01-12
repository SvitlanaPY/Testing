import unittest
from Testing.calc_ import Calc


class TestSum(unittest.TestCase):
    """
    Testing adding of values in calculator
    """

    def setUp(self) -> None:
        print('setUp')

    def test_Add_DataInputs(self):
        print('test_Add_DataInputs')
        self.assertIsInstance(Calc.sum(1, 2), int)
        self.assertIsInstance(Calc.sum(2.0, 2), float)
        self.assertIsInstance(Calc.sum(2, 3.0), float)

    def test_Add_Computing(self):
        print('test_Add_Computing')
        self.assertEqual(Calc.sum(0.0, 0), 0)
        self.assertEqual(Calc.sum(3, 3), 6.0)
        self.assertEqual(Calc.sum(-5, 2), -3)
        self.assertEqual(Calc.sum(105, 5.0), 110)

    def test_Add_RaiseExceptions(self):
        print('test_Add_RaiseExceptions')
        # self.assertRaises(TypeError, Calc.sum, "1", 2)
        with self.assertRaises(TypeError):
            Calc.sum("1", 2)

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()


# якщо у модулі є блок:
# if __name__ == '__main__':
#     unittest.main()
# то наш модуль test_division.py можна запустити в терміналі напряму, командою: ~$ python3 test_sum.py
# ця команда рівносильна запуску тестів через меню Run, це запуск модуля самостійно, а НЕ як імпортованого модуля
# (при такому запуску if __name__ == '__main__' і функція main() у unittest запустить наш файл test_sum.py з тестами як окремий модуль напряму)
# or
# запускаючи тести командою ~$ python3 -m unittest -v test_sum.py > output_unittesting.txt
# ми вказуємо інтерпретатору пайтон запустити наш модуль test_sum.py з тестами з бібліотеки unittest як імпортованого модуля
# ця команда - це скорочення для командної стрічки для запуску метода main() з бібліотеки unittest;
# при такому запуску наш модуль втрачає імя "main", а набуває імені модуля: __name__ == "test_sum",
# оск він імпортується і запускається з бібліотеки unittest, і блок if ... не буде виконуватись:
# if __name__ == '__main__':
#     unittest.main()
# тепер сама бібліотека unittest буде знати, що робити і як запустити імпортований модуль test_sum;
# results will be saved in file 'output_unittesting.txt'
