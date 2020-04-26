import unittest
from mock import patch
from HW6.matrix import matrix


class MyTestCase(unittest.TestCase):
    def test_matrix(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(matrix(arr), [24, 12, 8, 6])
        arr = [5, 5, 5, 5, 5, 5, 5, 5]
        self.assertEqual(matrix(arr), [78125, 78125, 78125, 78125, 78125, 78125, 78125, 78125])

    def test_mock_matrix(self):
        with patch('matrix.matrix') as mock_matrix:
            mock_matrix.return_value = [59049]*10
            arr = [3]*10
            self.assertEqual(mock_matrix(arr), [59049]*10)


if __name__ == '__main__':
    unittest.main()
