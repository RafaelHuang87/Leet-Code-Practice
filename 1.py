class Solution:
    def twoSum(nums, target):
        dict_nums = {}
        for i, num in enumerate(nums):
            if target - num not in dict_nums.keys():
                dict_nums[num] = i
            else:
                return [dict_nums[target - num], i]
