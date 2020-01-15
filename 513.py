# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        next_layer = [root]
        layer_value = []
        while next_layer:
            temp_next_layer = []
            layer_value = []
            for node in next_layer:
                if node.left:
                    temp_next_layer.append(node.left)
                if node.right:
                    temp_next_layer.append(node.right)
                layer_value.append(node.val)
            next_layer = temp_next_layer

        return layer_value[0]
