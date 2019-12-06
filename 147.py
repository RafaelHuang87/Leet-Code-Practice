# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        temp = []
        while cur:
            temp.append(cur.val)
            cur = cur.next

        for i in range(1, len(temp)):
            key = temp[i]
            j = i - 1
            while j >= 0:
                if temp[j] > key:
                    temp[j + 1] = temp[j]
                    temp[j] = key
                j = j - 1

        res = ListNode(0)
        cur = res
        for val in temp:
            cur.next = ListNode(val)
            cur = cur.next

        return res.next
