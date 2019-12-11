# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        view = []
        if root:
            level = [root]
            while level:
                view.append(level[-1].val)
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view