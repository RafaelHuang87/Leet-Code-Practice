# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        result = []

        def recursion(root):
            if root == None:
                return
            else:
                recursion(root.left)
                result.append(root.val)
                recursion(root.right)
        recursion(root)
        return result

head = TreeNode(1)
head.left = None
head.right = TreeNode(2)
head.right.left = TreeNode(3)
s = Solution()
print(s.inorderTraversal(head))
