# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = []
        self.inorder(root)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.right)
        self.res.append(root.val)
        self.inorder(root.left)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.res.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.res) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()