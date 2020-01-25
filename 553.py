class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        if len(nums) <= 2:
            return '/'.join(nums)
        else:
            return nums[0] + '/(' + '/'.join(nums[1:]) + ')'