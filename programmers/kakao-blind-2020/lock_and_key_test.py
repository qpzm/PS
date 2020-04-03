import unittest
from random import randint
from lock_and_key_before import solution

class SolutionTest(unittest.TestCase):
    def test_rotate2(self):
        self.assertEqual(rotate([[0, 1], [1, 0]]), [[1, 0], [0, 1]])

    def test_rotate3(self):
        self.assertEqual(rotate([[0, 0, 0], [0, 0, 0], [0, 1, 0]]),
                         [[0, 0, 0], [1, 0, 0], [0, 0, 0]])

    def test_rotate4(self):
        l = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
        self.assertEqual(rotate(rotate(rotate(rotate(l)))), l)

   # def test_is_all_one(self):
        # self.assertEqual(is_all_one([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), False)

    def test_solution_with_rotation1(self):
        self.assertTrue(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
                                  [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

    def test_solution_without_rotation(self):
        self.assertTrue(solution([[0, 1, 0], [0, 0, 0], [0, 0, 0]],
                                  [[1, 1, 1], [1, 1, 1], [1, 0, 1]]))

    def test_solution_with_rotation2(self):
        self.assertTrue(solution([[0, 1, 0], [1, 0, 0], [1, 0, 0]],
                                  [[1, 0, 1], [0, 1, 1], [0, 1, 1]]))

    def test_solution_with_rotation3(self):
        self.assertTrue(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                                  [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))

    def test_solution_with_rotation4(self):
        self.assertEqual(solution(
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1]]),
            True)

    def test_counterexample(self):
        key, lock = [[0, 0], [1, 1]], [[1, 1, 1], [1, 1, 0], [1, 1, 1]]
        self.assertTrue(solution(key, lock))


if __name__ == '__main__':
    unittest.main()
