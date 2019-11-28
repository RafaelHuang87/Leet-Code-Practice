# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        temp = dict()
        pre = head
        result = ListNode(0)
        cur = result
        while pre:
            if pre.val not in temp.keys():
                cur.next = ListNode(pre.val)
                cur = cur.next
                temp[pre.val] = 1
                pre = pre.next
            else:
                pre = pre.next

        return result.next

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
s = Solution()
re = s.deleteDuplicates(head)
while re:
    print(re.val)
    re = re.next