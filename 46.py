class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        res = []
        def dfs(nums = nums, path = []):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        dfs()
        return res
