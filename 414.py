class Solution:
    def thirdMax(self, nums: [int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums = sorted(set(nums), reverse=True)
        return nums[2]

s = Solution()
print(s.thirdMax([2,2,3,1]))