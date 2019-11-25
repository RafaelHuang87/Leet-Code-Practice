class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        nums.sort()
        res = []
        l = []

        def dfs(l, pre, nums):
            if len(nums) == 0:
                res.append(l[:])
            pre = None
            for i in range(len(nums)):
                if nums[i] == pre:
                    continue
                l.append(nums[i])
                dfs(l, nums[i], nums[:i] + nums[i + 1:])
                l.pop()
                pre = nums[i]

        dfs(l, None, nums)
        return res

s = Solution()
print(s.permuteUnique([1,1,2]))