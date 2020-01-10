class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for pos in range(32):
            bitCount = 0
            for i in range(len(nums)):
                bitCount += (nums[i] >> pos) & 1
            res += bitCount * (len(nums) - bitCount)
        return res
