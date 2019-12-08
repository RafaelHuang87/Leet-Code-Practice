class Solution:
    def maximumGap(self, nums: [int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_diff = 0
        i = 1
        while i <= len(nums) - 1:
            max_diff = max(max_diff, nums[i] - nums[i - 1])
            i += 1
        return max_diff

s = Solution()
print(s.maximumGap([3,6,9,1]))