import unittest
from tree_memory_bloat import preorder

class TreeTest(unittest.TestCase):
    def test_simple(self):
        inorder   = [1, 2, 3]
        postorder = [1, 3, 2]
        answer    = [2, 1, 3]
        self.assertEqual(preorder(inorder, postorder), answer)

    def test1(self):
        inorder   = [4, 1, 5, 2, 6, 3, 7]
        postorder = [4, 5, 1, 6, 7, 3, 2]
        answer    = [2, 1, 4, 5, 3, 6, 7]
        self.assertEqual(preorder(inorder, postorder), answer)

    def test2(self):
        inorder   = [4, 1, 2, 3, 7]
        postorder = [4, 1, 7, 3, 2]
        answer    = [2, 1, 4, 3, 7]
        self.assertEqual(preorder(inorder, postorder), answer)


if __name__ == '__main__':
    unittest.main()
