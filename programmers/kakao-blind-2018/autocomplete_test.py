import unittest
from autocomplete import solution

class AutoCompleteTest(unittest.TestCase):
    def test0(self):
        words = ["go", "gone", "guild"]
        self.assertEqual(7, solution(words))

    def test1(self):
        words = ["abc", "def", "ghi", "jklm"]
        self.assertEqual(4, solution(words))

    def test2(self):
        words = ["word","war","warrior","world"]
        self.assertEqual(15, solution(words))


if __name__ == '__main__':
    unittest.main()
