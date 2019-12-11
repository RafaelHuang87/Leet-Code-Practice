# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        curr, newList = head, None
        while curr:
            temp = curr.next
            curr.next = newList
            newList = curr
            curr = temp
        return newList