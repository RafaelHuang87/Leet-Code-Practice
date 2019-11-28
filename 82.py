# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        temp_dict = dict()
        pre = head
        while pre:
            if pre.val not in temp_dict.keys():
                temp_dict[pre.val] = 1
            else:
                temp_dict[pre.val] += 1
            pre = pre.next

        temp = []
        for i, value in temp_dict.items():
            if value > 1:
                continue
            else:
                temp.append(i)

        result = ListNode(0)
        cur = result
        for value in temp:
            cur.next = ListNode(value)
            cur = cur.next
        return result.next

