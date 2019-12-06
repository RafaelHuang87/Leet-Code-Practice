# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp1, temp2 = head, self.reverse(slow.next)
        slow.next = None
        while temp1 and temp2:
            cur = temp2
            temp2 = temp2.next
            cur.next = temp1.next
            temp1.next = cur
            temp1 = temp1.next.next

        return head

    def reverse(self, head):
        if not head or not head.next:
            return head

        p = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return p