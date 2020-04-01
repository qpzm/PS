import unittest
from zero_one_bfs import solve

class TestHideAndSeek(unittest.TestCase):
    def test0(self):
        self.assertEqual(solve(0, 100_000), 6)

    def test1(self):
        self.assertEqual(solve(5, 17), 2)

    def test2(self):
        self.assertEqual(solve(17, 5), 12)

    def test3(self):
        self.assertEqual(solve(5, 80), 0)

    def test4(self):
        self.assertEqual(solve(1, 16), 0)

if __name__ == '__main__':
    unittest.main()
