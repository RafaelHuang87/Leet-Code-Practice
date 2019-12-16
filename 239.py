class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        start, end, res = 0, k, []
        while end <= len(nums):
            print(nums[start:end])
            res.append(max(nums[start:end]))
            start, end = start + 1, end + 1
        return res

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))