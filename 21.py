# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not l1 and l2:
        #     return l2
        # if not l2 and l1:
        #     return l1
        # if not l1 and not l2:
        #     return None
        # temp = list()
        # pre1 = l1
        # pre2 = l2
        # while pre1:
        #     temp.append(pre1.val)
        #     pre1 = pre1.next
        #
        # while pre2:
        #     temp.append(pre2.val)
        #     pre2 = pre2.next
        # temp = sorted(temp)
        #
        # result = ListNode(temp[0])
        # cur = result
        # for i, value in enumerate(temp):
        #     if i == 0:
        #         continue
        #     cur.next = ListNode(value)
        #     cur = cur.next
        # return result
        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else :
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return first.next

s = Solution()
t1 = ListNode(1)
t1.next = ListNode(2)
t2 = ListNode(1)
t2.next = ListNode(3)
r = s.mergeTwoLists(t1, t2)
while r:
    print(r.val)
    r = r.next
