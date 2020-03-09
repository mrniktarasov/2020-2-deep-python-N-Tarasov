from unittest import TestCase, main
from array import ArrAddSub


class MyTestCase(TestCase):
    def test_array(self):
        ar1 = ArrAddSub(1, 3, 4, 7)
        ar2 = ArrAddSub(0, 2, 3, 4)
        self.assertEqual(ar1 + ar2, [1, 5, 7, 11])


if __name__ == '__main__':
    main()
