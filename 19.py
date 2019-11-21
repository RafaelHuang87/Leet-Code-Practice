# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = head
        length = 0
        while pre:
            pre = pre.next
            length += 1
        if length == 1:
            if n == 1:
                return None

        pos = length - n
        pre = head
        if pos == 0:
            return pre.next
        for i in range(length):
            if i == pos - 1:
                pre.next = pre.next.next
                return head
            else:
                pre = pre.next

head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
s = Solution()
t = s.removeNthFromEnd(head, 2)
while t:
    print(t.val)
    t = t.next




