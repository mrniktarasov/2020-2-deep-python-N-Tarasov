import unittest
from MedianFinder import MedianFinder


class MyTestCase(unittest.TestCase):
    def test_add_num(self):
        a = MedianFinder()
        a.add_num(1)
        a.add_num(8)
        a.add_num(5)
        a.add_num(-5)
        self.assertEqual(a.nums, [-5, 1, 5, 8])

    def test_find_median(self):
        a = MedianFinder()
        a.add_num(1)
        a.add_num(2)
        a.add_num(3)
        a.add_num(4)
        self.assertEqual(a.find_median(), 2.5)
        b = MedianFinder()
        b.add_num(-5)
        b.add_num(-3)
        b.add_num(2)
        b.add_num(8)
        self.assertEqual(b.find_median(), -0.5)
        c = MedianFinder()
        c.add_num(-5)
        self.assertEqual(c.find_median(), -5)


if __name__ == '__main__':
    unittest.main()
