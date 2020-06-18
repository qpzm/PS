import unittest
from tree_diameter import diameter

class TestTreeDiameter(unittest.TestCase):
    def test0(self):
        tree = {2: [(4, 4)], 4: [(2,4)]}
        self.assertEqual(diameter(tree, 4), (0, 4))

    def test1(self):
        tree = {2: [(4, 4)], 4: [(2,4), (5, 6)], 5: [(4,6)]}
        self.assertEqual(diameter(tree, 4), (10, 6))

    def test2(self):
        tree = {2: [(4, 4)], 4: [(2,4), (5, 6), (3, 3)], 5: [(4,6)], 3: [(4, 3)]}
        self.assertEqual(diameter(tree, 4), (10, 6))

    def test3(self):
        tree = {1: [(3, 2)], 2: [(4, 4)],  3: [(1, 2), (4, 3)],
                4: [(2, 4), (5, 6), (3, 3)], 5: [(4,6)]}
        self.assertEqual(diameter(tree, 4), (11, 6))

if __name__ == '__main__':
    unittest.main()
