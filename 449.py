# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        l = []

        def preOrder(root):
            if root:
                l.append(root.val)
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)
        return ' '.join(map(str, l))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        import collections
        vals = collections.deque([int(val) for val in data.split()])

        def buildTree(vals, minVal, maxVal):
            while vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                root = TreeNode(val)
                root.left = buildTree(vals, minVal, val)
                root.right = buildTree(vals, val, maxVal)
                return root

        return buildTree(vals, float('-inf'), float('inf'))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))