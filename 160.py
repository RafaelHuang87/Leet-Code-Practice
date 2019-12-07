# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        return p1

headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headB = ListNode(1)
headB.next = ListNode(3)
headB.next.next = ListNode(2)
headB.next.next.next = ListNode(3)
s = Solution()
res = s.getIntersectionNode(headA, headB)
while res:
    print(res.val)
    res = res.next