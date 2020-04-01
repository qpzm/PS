import unittest
from bsearch import solve

class BsearchTest(unittest.TestCase):
    def test_unsorted(self):
        self.assertEqual(solve([1, 2, 8, 9, 4], 3), 3)

    def test2(self):
        self.assertEqual(solve([1, 2, 3, 5, 8, 9, 10], 4), 2)

    def test3(self):
        self.assertEqual(solve([1, 2, 3, 5, 8, 9, 100000], 7), 1)

    def test4(self):
        self.assertEqual(solve([1, 1000, 2000, 5000, 8000, 90000, 100000], 6), 1999)

    def test5(self):
        self.assertEqual(solve([1, 90_000, 100_000], 3), 10_000)

    def test6(self):
        self.assertEqual(solve([1, 90_000, 100_000], 2), 99_999)

    def test7(self):
        self.assertEqual(solve([1, 1_000_000], 2), 999_999)


if __name__ == '__main__':
    unittest.main()
