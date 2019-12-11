class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        return sorted(nums)[-k]

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], k = 2))