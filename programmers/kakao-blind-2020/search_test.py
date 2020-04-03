import unittest
from search import solution

class SolutionTest(unittest.TestCase):
    def test_right(self):
        words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
        queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
        answer = [3, 2, 4, 1, 0]
        self.assertEqual(solution(words, queries), answer)

if __name__ == '__main__':
    unittest.main()
