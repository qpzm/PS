import unittest
from candidate_key import solution

class SolutionTest(unittest.TestCase):
    def test1(self):
        relation = [
            ["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]
        ]
        self.assertEqual(solution(relation), 2)

if __name__ == '__main__':
    unittest.main()
