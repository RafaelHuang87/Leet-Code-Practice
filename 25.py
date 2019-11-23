# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return None

        value = []
        result_temp = []
        temp = head
        while temp:
            value.append(temp.val)
            temp = temp.next

        if k > len(value):
            return head

        count = 0
        while count < len(value):
            if count + k < len(value):
                lst = (value[count: count + k])[::-1]
            else:
                lst = value[count:]

            count += k
            for i in lst:
                result_temp.append(i)

        result = ListNode(0)
        cur = result
        for num in result_temp:
            cur.next = ListNode(num)
            cur = cur.next

        return result.next