class Solution:
    def findMin(self, nums: [int]) -> int:
        return sorted(nums)[0]

s = Solution()
print(s.findMin([3,4,5,1,2]))