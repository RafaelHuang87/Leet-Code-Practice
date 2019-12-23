class Node:
    def __init__(self, dup, val):
        self.dup = dup
        self.val = val
        self.left = None
        self.right = None
        self.sum = 0
    def inDup(self):
        self.dup += 1

    def getDup(self):
        return self.dup

class Solution:
    def countSmaller(self, nums: [int]) -> [int]:
        counts = []
        root = Node(0, 0)
        for i in range(len(nums) - 1, -1, -1):
            root = self.insert(counts, root, nums[i], 0)

        return counts[::-1]

    def insert(self, counts, node, val, sum):
        if not node:
            node = Node(1, val)
            counts.append(sum)
        elif node.val == val:
            node.inDup()
            counts.append(sum + node.sum)
        elif node.val > val:
            node.sum += 1
            node.left = self.insert(counts, node.left, val, sum)
        else:
            node.right = self.insert(counts, node.right, val, sum + node.getDup() + node.sum)
        return node

s = Solution()
print(s.countSmaller([5,2,6,1]))