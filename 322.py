class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(0, len(coins)):
                if i >= coins[j] and dp[i - coins[j]] != -1:
                    if dp[i] == -1 or dp[i] > dp[i - coins[j]] + 1:
                        dp[i] = dp[i - coins[j]] + 1
        return dp[amount]
