class Solution:
    def maxNumber(self, nums1: [int], nums2: [int], k: int) -> [int]:
        res = []
        for i in range(max(k - len(nums2), 0), min(k, len(nums1)) + 1):
            res = max(res, self.merge(self.getMax(nums1, i), self.getMax(nums2, k-i)))
        return res

    def getMax(self, nums, k):
        stk, poped = [], len(nums) - k
        if poped == 0:
            return nums[:]
        if k == 0:
            return []
        for i in range(len(nums)):
            while len(stk) > 0 and poped > 0 and stk[-1] < nums[i]:
                stk.pop()
                poped -= 1
            stk.append(nums[i])
        return stk[:k]

    def merge(self, nums1, nums2):
        vec = []
        while len(nums1) + len(nums2) > 0:
            temp = nums1 if nums1 > nums2 else nums2
            vec.append(temp[0])
            del temp[0]
        return vec

s = Solution()
print(s.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))