import unittest
from bracket import solution

class SolutionTest(unittest.TestCase):
    def test_right(self):
        self.assertEqual(solution("(()())()"), "(()())()")

    def test1(self):
        self.assertEqual(solution(')('), '()')

    def test2(self):
        self.assertEqual(solution("()))((()"), "()(())()")

if __name__ == '__main__':
    unittest.main()
