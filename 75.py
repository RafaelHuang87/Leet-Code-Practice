class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        c0, c1, c2 = 0, 0, 0
        for value in nums:
            if value == 0:
                c0 += 1
            elif value == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0: c0 + c1] = [1] * c1
        nums[c0 + c1:] = [2] * c2


s = Solution()

