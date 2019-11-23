class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        flag = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == flag:
                nums.remove(nums[i])
            else:
                flag = nums[i]
                i += 1
        return len(nums)

s = Solution()
print(s.removeDuplicates([1,1,2]))