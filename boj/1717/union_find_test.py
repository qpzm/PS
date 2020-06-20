import unittest
from union_find import UnionFind

class UnionFindTest(unittest.TestCase):
    def test0(self):
        u = UnionFind(3)
        u.union(0, 1)
        u.union(0, 2)
        u.union(2, 3)
        self.assertTrue(u.same_set(1, 2))
        self.assertTrue(u.same_set(1, 3))

    def test_find_the_root_when_unioning(self):
        u = UnionFind(7)
        u.union(0, 1)
        u.union(2, 3)
        u.union(1, 3)
        self.assertTrue(u.same_set(0, 2))
        u.union(4, 5)
        u.union(6, 7)
        u.union(4, 6)
        u.union(3, 4)
        self.assertTrue(u.same_set(0, 2))

if __name__ == "__main__":
    unittest.main()
