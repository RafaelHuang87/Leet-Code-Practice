# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))

            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))

            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))

        return res

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.right = TreeNode(5)
s = Solution()
print(s.binaryTreePaths(head))



