# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        que = [root]
        if root is None:
            return res
        while que:
            tempList = []
            for i in range(len(que)):
                node = que.pop(0)
                tempList.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(max(tempList))
        return res
