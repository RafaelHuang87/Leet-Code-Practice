# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        n = inorder.index(root.val)
        root.left = self.buildTree(inorder[:n], postorder[:n])
        root.right = self.buildTree(inorder[n + 1:], postorder[n:-1])
        return root
