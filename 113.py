# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        self.total = sum

        def caculate(root, sum, templist):
            if not root:
                return
            if not root.left and not root.right:
                if root.val + sum == self.total:
                    self.res.append(templist + [root.val])
            if root.left:
                caculate(root.left, sum + root.val, templist + [root.val])
            if root.right:
                caculate(root.right, sum + root.val, templist + [root.val])

        caculate(root, 0, [])
        return self.res