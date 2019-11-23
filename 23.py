# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        temp = []
        if not lists:
            return None
        for term in lists:
            while term:
                temp.append(term.val)
                term = term.next

        temp = sorted(temp)
        head = ListNode(0)
        first = head
        for value in temp:
            first.next = ListNode(value)
            first = first.next

        return head.next