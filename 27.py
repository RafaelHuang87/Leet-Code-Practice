class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        if not nums or val == None:
            return 0
        i = 0
        nums.sort()
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)


s = Solution()
print(s.removeElement([2,2,2], 0))