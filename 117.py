# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        M = Node(0, None, None, None)
        N = M
        while root != None:
            if root.left != None:
                N.next = root.left
                N = N.next
            if root.right != None:
                N.next = root.right
                N = N.next
            root = root.next
            if root == None:
                root = M.next
                N = M
                N.next = None
        return head
