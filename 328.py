# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_head = odd = head.next
        even = head
        while even and even.next and odd and odd.next:
            even.next = even.next.next
            even = even.next
            odd.next = odd.next.next
            odd = odd.next

        even.next = odd_head

        return head