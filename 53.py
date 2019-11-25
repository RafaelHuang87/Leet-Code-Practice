class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        cur = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            if cur < 0:
                cur = nums[i]
            else:
                cur += nums[i]

            result = max(result, cur)
        return result

