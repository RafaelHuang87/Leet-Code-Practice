class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for val in nums:
            last, now = now, max(last + val, now)
        return now