import unittest
from hotel_naive import solution as naive_solution

class SolutionTest(unittest.TestCase):
    def test_right(self):
        self.assertEqual(naive_solution(10, [1,3,4,1,3,1]), [1,3,4,2,5,6])


if __name__ == '__main__':
    unittest.main()
