# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode):
        self.re = -pow(2, 31)

        self.recursion(root)
        return self.re

    def recursion(self, root):
        if root is None:
            return 0
        left = max(0, self.recursion(root.left))
        right = max(0, self.recursion(root.right))
        self.re = max(self.re, root.val + left + right)
        return max(root.val, root.val + max(left, right))


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
s = Solution()
print(s.maxPathSum(head))
