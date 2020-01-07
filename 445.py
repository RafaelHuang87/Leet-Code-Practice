# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = "", ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        res = str(int(num1) + int(num2))
        ans = ListNode(0)
        cur = ans
        for i in res:
            cur.next = ListNode(i)
            cur = cur.next
        return ans.next

num1 = ListNode(7)
num1.next = ListNode(2)
num1.next.next = ListNode(4)
num1.next.next.next = ListNode(3)
num2 = ListNode(5)
num2.next = ListNode(6)
num2.next.next = ListNode(4)
print(Solution().addTwoNumbers(num1, num2))