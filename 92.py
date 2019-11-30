# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        pre = head
        temp_list = [0]
        while pre:
            temp_list.append(pre.val)
            pre = pre.next

        while m <= n:
            temp_list[m], temp_list[n] = temp_list[n], temp_list[m]
            m += 1
            n -= 1

        result = ListNode(0)
        cur = result
        for i in range(1, len(temp_list)):
            cur.next = ListNode(temp_list[i])
            cur = cur.next

        return result.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s = Solution()
re = s.reverseBetween(head, 2, 4)
while re:
    print(re.val)
    re = re.next