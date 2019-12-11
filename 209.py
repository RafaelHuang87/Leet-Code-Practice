class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r, csum = 0, 0, 0
        res = float('inf')
        while r < len(nums):
            csum += nums[r]
            while csum >= s:
                res = min(res, r - l + 1)
                csum -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0
