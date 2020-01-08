class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))

s = Solution()
print(s.findDisappearedNumbers([1, 1]))