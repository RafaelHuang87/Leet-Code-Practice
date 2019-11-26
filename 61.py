# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        temp = []
        p = head
        while p:
            temp.append(p.val)
            p = p.next
        if k == 0:
            return head
        trans = k % len(temp)
        temp_result = temp[len(temp) - trans:] + temp[:len(temp) - trans]
        result = ListNode(0)
        cur = result
        for value in temp_result:
            cur.next = ListNode(value)
            cur = cur.next
        return result.next



s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
r = s.rotateRight(head, 2)
while r:
    print(r.val)
    r = r.next
