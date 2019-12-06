# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid, slow.next = slow.next, None
        l1 = self.sortList(head)
        l2 = self.sortList(mid)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        head = ListNode(0)
        cur = head
        if not l1:
            return l2
        if not l2:
            return l1

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 if l1 else l2
        return head.next