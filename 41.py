class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        if not nums:
            return 1
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i + 1: return i + 1
        return len(nums) + 1


s = Solution()
print(s.firstMissingPositive([2]))
