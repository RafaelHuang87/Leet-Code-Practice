class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        inc, dec = 1, 1
        for x in range(1, n):
            if nums[x] > nums[x - 1]:
                inc = dec + 1
            elif nums[x] < nums[x - 1]:
                dec = inc + 1
        return max(inc, dec)
