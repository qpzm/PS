# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(node):
    if node is None:
        return -1, 0
    else:
        left_radius, left_diameter = maxDepth(node.left)
        right_radius, right_diameter = maxDepth(node.right)
        return 1 + max(left_radius, right_radius), max(2 + left_radius + right_radius, left_diameter, right_diameter)

def diameterOfBinaryTree(root):
    return maxDepth(root)[1]
