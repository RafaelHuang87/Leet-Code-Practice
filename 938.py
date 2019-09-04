"""
Solution for Leet Code 938.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        def dfs(node):
            if node is not None:
                if L <= node.val and node.val <= R:
                    self.sum += node.val
                if node.val > L:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        dfs(root)
        return self.sum