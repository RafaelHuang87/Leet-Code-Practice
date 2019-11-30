# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if not nums:
            return None
        length = len(nums)
        root = TreeNode(nums[length // 2])
        root.left = self.sortedArrayToBST(nums[:length // 2])
        root.right = self.sortedArrayToBST(nums[length // 2 + 1:])

        return root