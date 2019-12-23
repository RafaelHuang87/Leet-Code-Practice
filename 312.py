class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = []
        for i in range(len(nums)): dp.append(len(nums) * [0])
        n = len(nums)
        for i in range(2, n):
            for a in range(n - i):
                for b in range(a + 1, a + i):
                    dp[a][a + i] = max(dp[a][a + i], dp[a][b] + dp[b][a + i] + nums[a] * nums[b] * nums[a + i])
        return dp[0][-1]
