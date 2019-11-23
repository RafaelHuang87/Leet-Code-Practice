class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            nums.sort()
            return

        j = i - 1
        while i < len(nums) - 1 and nums[i + 1] > nums[j]:
            i += 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[j + 1:] = sorted(nums[j + 1:])
        print(nums)

s = Solution()
print(s.nextPermutation([1,2,3,6,7]))
