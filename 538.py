# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.order(root)
        return root

    def order(self, root):
        if not root:
            return
        self.order(root.right)
        self.sum += root.val
        root.val = self.sum
        self.order(root.left)