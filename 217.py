class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        return len(nums) != len(set(nums))

s = Solution()
print(s.containsDuplicate([1,2,3,1]))