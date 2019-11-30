# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_val(node, min_v, max_v):
            if node == None:
                return True
            if node.left != None:
                if node.left.val >= node.val or node.left.val <= min_v:
                    return False

            if node.right != None:
                if node.right.val <= node.val or node.right.val >= max_v:
                    return False

            return is_val(node.left, min_v, node.val) and is_val(node.right, node.val, max_v)

        return is_val(root, -pow(2, 32), pow(2, 32) - 1)

head = TreeNode(2)
head.left = TreeNode(1)
head.right = TreeNode(3)
s = Solution()
print(s.isValidBST(head))