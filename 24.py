# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        temp = ListNode(0)
        temp.next = head
        p = temp
        q = temp.next
        while q and q.next:
            p.next = q.next
            q.next = p.next.next
            p.next.next = q
            p = q
            q = q.next

        return temp.next