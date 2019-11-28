# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = ListNode(0)
        greater = ListNode(0)
        cur = less
        pre = head
        while pre:
            if pre.val < x:
                cur.next = ListNode(pre.val)
                cur = cur.next
            pre = pre.next

        pre = head
        cur2 = greater
        while pre:
            if pre.val >= x:
                cur2.next = ListNode(pre.val)
                cur2 = cur2.next
            pre = pre.next

        cur.next = greater.next
        return less.next
