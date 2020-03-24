import unittest
from MaxHeap import MaxHeap

class MyTestCase(unittest.TestCase):
    def test_MaxHeap(self):
        a = MaxHeap()
        a.push(1)
        a.push(3)
        a.push(4)
        self.assertEqual(a.heap, [4, 3, 1])

    def test_heapify(self):
        a = MaxHeap()
        a.heapify([5, 2, 5, 9, 89, 0])
        self.assertEqual(a.heap, [89, 9, 5, 5, 2, 0])


if __name__ == '__main__':
    unittest.main()
