import unittest
from LRU import ICache
from collections import OrderedDict


class MyTestCase(unittest.TestCase):
    def test_set(self):
        a = ICache(3)
        a.set(1, '111')
        self.assertEqual(a.cache, OrderedDict([(1, '111')]))
        a.set(2, '222')
        a.set(3, '333')
        self.assertEqual(a.cache, OrderedDict([(1, '111'), (2, '222'), (3, '333')]))
        a.set(4, '444')
        self.assertEqual(a.cache, OrderedDict([(1, '111'), (2, '222'), (4, '444')]))

    def test_get(self):
        a = ICache(15)
        a.set(1, '111')
        a.set(2, '222')
        a.set(3, '333')
        self.assertEqual(a.get(1), '111')
        self.assertEqual(a.get(2), '222')
        self.assertEqual(a.get(3), '333')

    def test_delete(self):
        a = ICache(15)
        a.set(1, '111')
        a.set(2, '222')
        a.set(3, '333')
        a.delete(1)
        self.assertEqual(a.cache, OrderedDict([(2, '222'), (3, '333')]))
        a.delete(2)
        self.assertEqual(a.cache, OrderedDict([(3, '333')]))
        a.delete(3)
        self.assertEqual(a.cache, OrderedDict())


if __name__ == '__main__':
    unittest.main()
