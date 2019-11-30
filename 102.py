# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        queue = [root]
        res = []
        if not root:
            return []
        while queue:
            templist = []
            templen = len(queue)
            for i in range(templen):
                temp = queue.pop(0)
                templist.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            res.append(templist)
        return res

