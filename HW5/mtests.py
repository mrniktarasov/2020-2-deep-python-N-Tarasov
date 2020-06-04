import unittest
from matrix import Matrix


class MyTestCase(unittest.TestCase):
    def test_add_matrix(self):
        first_matrix = Matrix([[1, 2], [3, 4]])
        second_matrix = Matrix([[5, 6], [7, 8]])
        self.assertEqual(first_matrix.add_matrix(second_matrix), [[6, 8], [10, 12]])

    def test_mult_matrix(self):
        first_matrix = Matrix([[1, 2], [3, 4]])
        second_matrix = Matrix([[5, 6], [7, 8]])
        self.assertEqual(first_matrix.mult_matrix(second_matrix), [[19, 22], [43, 50]])

    def test_mult_number(self):
        first_matrix = Matrix([[4, 5], [3, 6]])
        second_argument = 2
        self.assertEqual(first_matrix.mult_number(second_argument), [[8, 10], [6, 12]])

    def test_divide_number(self):
        first_matrix = Matrix([[6, 9], [6, 12]])
        second_argument = 3
        self.assertEqual(first_matrix.divide_number(second_argument), [[2, 3], [2, 4]])

    def test_transpose(self):
        matrix = Matrix([[3, 6, 9], [12, 15, 18]])
        self.assertEqual(matrix.transpose(), [[3, 12], [6, 15], [9, 18]])

    def test_contains_positive(self):
        matrix = Matrix([[3, 6, 9], [12, 15, 18]])
        self.assertTrue(matrix.contains(9))

    def test_contains_negative(self):
        matrix = Matrix([[3, 6, 9], [12, 15, 18]])
        self.assertFalse(matrix.contains(10))

    def test_access_by_coords(self):
        matrix = Matrix([[3, 6, 9], [12, 15, 18]])
        self.assertEqual(matrix.get_element((1, 1)), 15)


if __name__ == '__main__':
    unittest.main()
