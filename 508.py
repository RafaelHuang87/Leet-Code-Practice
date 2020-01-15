# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.val = []
        self.get_sum(root)
        import collections
        count = collections.Counter(self.val)
        res = sorted(count.items(), key=lambda item: item[1], reverse=True)
        return [res[0][0]]

    def get_sum(self, root):
        if not root:
            return 0
        sums = self.get_sum(root.left) + root.val + self.get_sum(root.right)
        self.val.append(sums)
        return sums
