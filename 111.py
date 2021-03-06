# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min([self.minDepth(root.left), self.minDepth(root.right)])

head = TreeNode(1)
head.left = TreeNode(2)
# head.left = TreeNode(9)
# head.right = TreeNode(20)
# head.right.left = TreeNode(15)
# head.right.right = TreeNode(7)
s = Solution()
print(s.minDepth(head))