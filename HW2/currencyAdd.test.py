import unittest
from currencyAdd import CurrencyAdder


class MyTestCase(unittest.TestCase):
    def test_add(self):
        c1 = CurrencyAdder(4, 'RUB')
        c2 = CurrencyAdder(5, 'USD')
        c3 = c1 + c2
        self.assertEqual(c3.value, 369.94)
        c3 = c1 + 6
        self.assertEqual(c3.value, 10)
        c1 = CurrencyAdder(4, 'USD')
        c2 = CurrencyAdder(5, 'CNY')
        c3 = c1 + c2
        self.assertEqual(c3.value, 4.71)
        self.assertEqual(str(c1 + c2), '4.71 USD')
        c1 = CurrencyAdder(4)
        c2 = CurrencyAdder(5, 'USD')
        c3 = c1 + c2
        self.assertEqual(c3.value, 9)
        c1 = CurrencyAdder(4, 'USD')
        c2 = CurrencyAdder(5)
        c3 = c1 + c2
        self.assertEqual(c3.value, 9)

    def test_repr(self):
        c1 = CurrencyAdder(5, 'USD')
        self.assertEqual(c1.__repr__(), 'CurrencyAdder: {value: 5, name: USD}')

    def test_str(self):
        c1 = CurrencyAdder(5, 'USD')
        self.assertEqual(c1.__str__(), '5 USD')


if __name__ == '__main__':
    unittest.main()
