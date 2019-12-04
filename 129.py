# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [0]

        def dfs(root, s):
            if not root.left and not root.right:
                res[0] += int(s + str(root.val))
                return
            if root.left:
                dfs(root.left, s + str(root.val))
            if root.right:
                dfs(root.right, s + str(root.val))

        dfs(root, '')
        return res[0]
