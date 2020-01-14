# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> [int]:
        self.temp = dict()
        self.order(root)
        self.temp = sorted(self.temp.items(), key=lambda item: item[1], reverse=True)
        return [x[0] for x in self.temp if x[1] == self.temp[0][1]]

    def order(self, root):
        if not root:
            return
        if root.val not in self.temp:
            self.temp[root.val] = 1
        else:
            self.temp[root.val] += 1
        if root.left:
            self.order(root.left)
        if root.right:
            self.order(root.right)

s = Solution()
head = TreeNode(1)
head.right = TreeNode(2)
head.right.left = TreeNode(2)
print(s.findMode(head))