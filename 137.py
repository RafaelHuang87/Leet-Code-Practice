class Solution:
    def singleNumber(self, nums: [int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2

s = Solution()
print(s.singleNumber([0,1,0,1,0,1,99]))