# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.temp = []
        self.preorder(root)
        return sorted(self.temp)[k - 1]

    def preorder(self, root: TreeNode):
        if not root:
            return root
        self.preorder(root.left)
        self.temp.append(root.val)
        self.preorder(root.right)

head = TreeNode(3)
head.left = TreeNode(1)
head.right = TreeNode(4)
head.left.right = TreeNode(2)
s = Solution()
print(s.kthSmallest(head, 1))