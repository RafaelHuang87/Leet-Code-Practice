# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root

        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right

        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
