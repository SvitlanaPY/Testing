from unittest import TestCase
from unittests_testing.vector_ import Vector

class TestVector(TestCase):
    def setUp(self) -> None:
        self.vector_1 = Vector(1, 1, 1)
        self.vector_2 = Vector(1, -1, 0)


    def test_InputDataType(self):
        self.assertIsInstance(self.vector_1.x, int)
        self.assertIsInstance(self.vector_1.y, int)
        self.assertIsInstance(self.vector_1.z, int)

    def test_Add_Two_Vectors(self):
        vector_3 = self.vector_1 + self.vector_2
        self.assertIsInstance(vector_3, Vector)

    def test_Multiply_Two_Vectors(self):
        mul = self.vector_1 * self.vector_2
        # self.assertIsInstance(mul, int)
        self.assertIsInstance(mul, Vector)

