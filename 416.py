class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2 == 1:
            return False
        nums = sorted(nums, key=lambda x: -x)
        target = sums // 2
        return self.dfs(nums, target, 0)

    def dfs(self, nums, target, k):
        if 0 == target:
            return True
        elif k < len(nums) and nums[k] > target:
            return False
        else:
            for i in range(k, len(nums)):
                if self.dfs(nums, target - nums[i], i + 1):
                    return True
        return False
