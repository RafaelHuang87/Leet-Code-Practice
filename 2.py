# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 1
        num_x1 = 0
        while l1:
            num_x1 += l1.val * i
            i *= 10
            l1 = l1.next
        i = 1
        num_x2 = 0
        while l2:
            num_x2 += l2.val * i
            i *= 10
            l2 = l2.next
        result = str(num_x1 + num_x2)[::-1]
        r = l = ListNode(0)
        for s in result:
            l.next = ListNode(int(s))
            l = l.next
        return r.next