class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp, pre = [1] * len(nums), [-1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre[i] = j

        ind = dp.index(max(dp))
        res = []
        while ind != -1:
            res.append(nums[ind])
            ind = pre[ind]
        return res