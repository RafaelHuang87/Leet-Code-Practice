"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        res = head
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next, head.child.prev, head.child = head.child, head, None
            elif head.next == None and stack:
                node = stack.pop()
                head.next, node.prev = node, head
            head = head.next
        return res
