# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(0)
        cur = res
        while head:
            if head.val != val:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
        return res.next



s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
# head.next.next.next = ListNode(3)
res = s.removeElements(head, 6)
while res:
    print(res.val)
    res = res.next