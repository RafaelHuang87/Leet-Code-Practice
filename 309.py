class Solution:
    def maxProfit(self, prices: [int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        for i, price in enumerate(prices):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -price
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[-1][0] if prices else 0

s = Solution()
print(s.maxProfit([1, 2, 3, 0, 2]))
