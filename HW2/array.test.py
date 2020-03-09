from unittest import TestCase, main
from arrayAddSub import ArrAddSub


class MyTestCase(TestCase):
    def test_add(self):
        ar1 = ArrAddSub(1, 3, 4, 7)
        ar2 = ArrAddSub(0, 2, 3, 4)
        self.assertEqual(ar1 + ar2, [1, 5, 7, 11])
        ar1 = ArrAddSub(1, 3, 4)
        ar2 = ArrAddSub(0, 2, 3, 4)
        self.assertEqual(ar1 + ar2, [1, 5, 7, 4])
        ar1 = ArrAddSub(0)
        ar2 = ArrAddSub(0)
        self.assertEqual(ar1 + ar2, [0])

    def test_sub(self):
        ar1 = ArrAddSub(1, 3, 4, 7)
        ar2 = ArrAddSub(0, 2, 3, 6)
        self.assertEqual(ar1 - ar2, [1, 1, 1, 1])
        ar1 = ArrAddSub(1, 3, 4)
        ar2 = ArrAddSub(0, 2, 3, 6)
        self.assertEqual(ar1 - ar2, [1, 1, 1, -6])

    def test_eq(self):
        ar1 = ArrAddSub(1, 1)
        ar2 = ArrAddSub(1, 1)
        self.assertEqual(ar1 == ar2, True)
        ar2 = ArrAddSub(1, 2)
        self.assertEqual(ar1 == ar2, False)

    def test_ne(self):
        ar1 = ArrAddSub(1, 1)
        ar2 = ArrAddSub(1, 1)
        self.assertEqual(ar1 != ar2, False)
        ar2 = ArrAddSub(1, 2)
        self.assertEqual(ar1 != ar2, True)

    def test_lt(self):
        ar1 = ArrAddSub(1, 1)
        ar2 = ArrAddSub(1, 3)
        self.assertEqual(ar1 < ar2, True)
        ar1 = ArrAddSub(1, 2, 8)
        self.assertEqual(ar1 < ar2, False)

    def test_gt(self):
        ar1 = ArrAddSub(1, 4)
        ar2 = ArrAddSub(1, 3)
        self.assertEqual(ar1 > ar2, True)
        ar2 = ArrAddSub(1, 2, 8)
        self.assertEqual(ar1 > ar2, False)

    def test_le(self):
        ar1 = ArrAddSub(1, 1)
        ar2 = ArrAddSub(1, 1)
        self.assertEqual(ar1 <= ar2, True)
        ar2 = ArrAddSub(1, 2, 8)
        self.assertEqual(ar1 <= ar2, True)
        ar2 = ArrAddSub(1)
        self.assertEqual(ar1 <= ar2, False)

    def test_ge(self):
        ar1 = ArrAddSub(1, 8)
        ar2 = ArrAddSub(1, 4)
        self.assertEqual(ar1 >= ar2, True)
        ar2 = ArrAddSub(1, 8)
        self.assertEqual(ar1 >= ar2, True)
        ar2 = ArrAddSub(1, 2, 5, 6)
        self.assertEqual(ar1 >= ar2, False)


if __name__ == '__main__':
    main()
