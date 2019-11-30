# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return self.sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        length = len(nums)
        root = TreeNode(nums[length // 2])
        root.left = self.sortedArrayToBST(nums[:length // 2])
        root.right = self.sortedArrayToBST(nums[length // 2 + 1:])

        return root