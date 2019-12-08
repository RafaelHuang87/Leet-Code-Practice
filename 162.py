class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        return nums.index(max(nums))