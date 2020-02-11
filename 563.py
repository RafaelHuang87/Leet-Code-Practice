# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        sum_tree, tilt_tree = self.sum_and_tilt(root)
        return tilt_tree

    def sum_and_tilt(self, root):
        if not root:
            return 0, 0
        sum_left, tilt_left = self.sum_and_tilt(root.left)
        sum_right, tilt_right = self.sum_and_tilt(root.right)
        return sum_left + sum_right + root.val, abs(sum_left - sum_right) + tilt_left + tilt_right