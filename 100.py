# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            l = self.isSameTree(p.left, q.left)
            r = self.isSameTree(p.right, q.right)
            return l and r
        else:
            return False




p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)
s = Solution()
print(s.isSameTree(p, q))