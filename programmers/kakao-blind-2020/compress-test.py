import unittest
from compress import solution

class SolutionTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution('abcd'), 4)

    def test2(self):
        self.assertEqual(solution('aaabcd'), 5)

    def test3(self):
        self.assertEqual(solution('aabbaccc'), 7)

    def test4(self):
        self.assertEqual(solution('aaaa'), 2)

    def test5(self):
        self.assertEqual(solution('abab'), 3)

    def test6(self):
        self.assertEqual(solution('a'), 1)

if __name__ == '__main__':
    unittest.main()
