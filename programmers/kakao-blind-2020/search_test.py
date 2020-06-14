import unittest
from search import solution, Node

class SolutionTest(unittest.TestCase):
    def test_put0(self):
        tree = Node()
        tree.put('abc')
        self.assertEqual(1, tree.children[0].children[1].children[2].count[0])

        tree.put('abd')
        self.assertEqual(1, tree.children[0].children[1].children[3].count[0])

    def test_search0(self):
        tree = Node()
        tree.put('abc')
        self.assertEqual(1, tree.search('ab?'))

    def test_search_question0(self):
        tree = Node()
        tree.put('abc')
        tree.put('abd')
        tree.put('abde')
        self.assertEqual(2, tree.search('a??'))

    def test_right(self):
        words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
        queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
        answer = [3, 2, 4, 1, 0]
        self.assertEqual(solution(words, queries), answer)

if __name__ == '__main__':
    unittest.main()
