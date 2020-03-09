import unittest
from currencyAdd import CurrencyAdder


class MyTestCase(unittest.TestCase):
    def test_add(self):
        c1 = CurrencyAdder(4, 'RUB')
        c2 = CurrencyAdder(5, 'USD')
        self.assertEqual(c1 + c2, 341.59)
        self.assertEqual(c1 + 6, 10)

    def test_repr(self):
        c1 = CurrencyAdder(5, 'USD')
        self.assertEqual(c1.__repr__(), '{value: 5, name: USD, rub: %s}' % str(c1.rub))

    def test_str(self):
        c1 = CurrencyAdder(5, 'USD')
        self.assertEqual(c1.__str__(), 'Currency (value= 5, age= USD, rub= %s)' % str(c1.rub))


if __name__ == '__main__':
    unittest.main()
